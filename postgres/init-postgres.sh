#!/bin/bash

# https://airflow.apache.org/docs/apache-airflow/stable/_images/airflow_erd.svg


set -e

ENV_FILE="/docker-entrypoint-initdb.d/.env"

if [ -f "$ENV_FILE" ]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
else
  echo "Error: .env file not found at $ENV_FILE."
  exit 1
fi

export POSTGRES_USER="${POSTGRES_USER:-blewy}"
export POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-Password123456789}"
export POSTGRES_DB="${POSTGRES_DB:-blewy}"
export POSTGRES_HOST="${POSTGRES_HOST:-postgres}"
export POSTGRES_PORT="${POSTGRES_PORT:-5432}"
export POSTGRES_ROLE="${POSTGRES_ROLE:-blewy}"
export PGPASSWORD="${POSTGRES_PASSWORD}"

if [ -z "$POSTGRES_USER" ]; then
  echo "Error: POSTGRES_USER is not set."
  exit 1
fi

if [ -z "$POSTGRES_PASSWORD" ]; then
  echo "Error: POSTGRES_PASSWORD is not set."
  exit 1
fi

if [ -z "$POSTGRES_DB" ]; then
  POSTGRES_DB=$POSTGRES_USER
fi

export PATH=$PATH:/usr/lib/postgresql/16/bin

: "${PGDATA:=/var/lib/postgresql/data}"

if [ ! -x "$0" ]; then
  chmod +x "$0"
fi

if [ ! -d "$PGDATA" ]; then
  mkdir -p "$PGDATA"
  chown postgres:postgres "$PGDATA"
fi

chown -R postgres:postgres "$PGDATA"

sed -i "s/^#listen_addresses = .*/listen_addresses = '*'/" "$PGDATA/postgresql.conf"

echo "host all all 0.0.0.0/0 md5" >> "$PGDATA/pg_hba.conf"
echo "host all all ::/0 md5" >> "$PGDATA/pg_hba.conf"

initialize_database() {
  local db_name=$1
  local sql_script=$2

  echo "Initializing database: $db_name"

  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -tc "SELECT 1 FROM pg_database WHERE datname = '$db_name';" | grep -q 1 || psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE DATABASE \"$db_name\" OWNER \"$POSTGRES_USER\";"

  psql -U "$POSTGRES_USER" -d "$db_name" -f "$sql_script"
}

grant_privileges() {
  local db_name=$1
  psql -U "$POSTGRES_USER" -d "$db_name" -c "GRANT ALL PRIVILEGES ON DATABASE \"$db_name\" TO ${POSTGRES_ROLE};"
  psql -U "$POSTGRES_USER" -d "$db_name" -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${POSTGRES_ROLE};"
  psql -U "$POSTGRES_USER" -d "$db_name" -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${POSTGRES_ROLE};"
}

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -tc "SELECT 1 FROM pg_roles WHERE rolname= '${POSTGRES_ROLE}';" | grep -q 1 || psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE ROLE ${POSTGRES_ROLE} WITH LOGIN PASSWORD '${POSTGRES_PASSWORD}';"

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "ALTER ROLE ${POSTGRES_ROLE} CREATEDB;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO ${POSTGRES_ROLE};"

grant_privileges "$POSTGRES_DB"

cat <<EOF > /tmp/blewy.sql
CREATE SCHEMA IF NOT EXISTS public;
GRANT ALL ON SCHEMA public TO ${POSTGRES_ROLE};
GRANT ALL ON SCHEMA public TO public;

-- Create other required tables for blewy
CREATE TABLE IF NOT EXISTS registered_model (
    name VARCHAR(256) PRIMARY KEY,
    creation_time TIMESTAMP,
    last_updated_time TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registered_model_tag (
    name VARCHAR(256) NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(250),
    PRIMARY KEY (name, key)
);

CREATE TABLE IF NOT EXISTS model_version (
    name VARCHAR(256) NOT NULL,
    version BIGINT NOT NULL,
    creation_time TIMESTAMP,
    last_updated_time TIMESTAMP,
    description TEXT,
    user_id VARCHAR(256),
    current_stage VARCHAR(20),
    source VARCHAR(512),
    run_id VARCHAR(32),
    status VARCHAR(20),
    status_message VARCHAR(500),
    PRIMARY KEY (name, version)
);

CREATE TABLE IF NOT EXISTS model_version_tag (
    name VARCHAR(256) NOT NULL,
    version BIGINT NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(250),
    PRIMARY KEY (name, version, key)
);

CREATE TABLE IF NOT EXISTS model_version_alias (
    name VARCHAR(256) NOT NULL,
    version BIGINT NOT NULL,
    alias VARCHAR(64) NOT NULL,
    PRIMARY KEY (name, alias)
);

CREATE TABLE IF NOT EXISTS experiments_tag (
    experiment_id BIGINT NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(500),
    PRIMARY KEY (experiment_id, key)
);

CREATE TABLE IF NOT EXISTS run (
    run_uuid VARCHAR(32) PRIMARY KEY,
    name VARCHAR(250),
    source_type VARCHAR(20),
    source_name VARCHAR(500),
    entry_point_name VARCHAR(50),
    user_id VARCHAR(256),
    status VARCHAR(20),
    start_time BIGINT,
    end_time BIGINT,
    source_version VARCHAR(50),
    lifecycle_stage VARCHAR(20),
    artifact_uri VARCHAR(200),
    experiment_id BIGINT
);

CREATE TABLE IF NOT EXISTS run_tag (
    run_uuid VARCHAR(32) NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(250),
    PRIMARY KEY (run_uuid, key)
);

CREATE TABLE IF NOT EXISTS params (
    run_uuid VARCHAR(32) NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(250),
    PRIMARY KEY (run_uuid, key)
);

CREATE TABLE IF NOT EXISTS metrics (
    key VARCHAR(250) NOT NULL,
    value DOUBLE PRECISION,
    timestamp BIGINT,
    step BIGINT,
    is_nan BOOLEAN,
    run_uuid VARCHAR(32) NOT NULL,
    PRIMARY KEY (run_uuid, key, timestamp, step)
);

CREATE TABLE IF NOT EXISTS tags (
    run_uuid VARCHAR(32) NOT NULL,
    key VARCHAR(250) NOT NULL,
    value VARCHAR(500),
    PRIMARY KEY (run_uuid, key)
);

CREATE TABLE IF NOT EXISTS latest_metrics (
    run_uuid VARCHAR(32) NOT NULL,
    key VARCHAR(250) NOT NULL,
    value DOUBLE PRECISION,
    timestamp BIGINT,
    step BIGINT,
    is_nan BOOLEAN,
    PRIMARY KEY (run_uuid, key)
);

-- Grant privileges on all tables and sequences
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${POSTGRES_ROLE};
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${POSTGRES_ROLE};

-- Grant usage and select/update on all sequences
DO \$\$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = 'public') LOOP
        EXECUTE 'GRANT USAGE, SELECT, UPDATE ON SEQUENCE ' || quote_ident(r.sequence_name) || ' TO ${POSTGRES_ROLE};';
    END LOOP;
END \$\$;

-- Grant execute on all functions
DO \$\$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT routine_name FROM information_schema.routines WHERE routine_schema = 'public') LOOP
        EXECUTE 'GRANT EXECUTE ON FUNCTION ' || quote_ident(r.routine_name) || ' TO ${POSTGRES_ROLE};';
    END LOOP;
END \$\$;
EOF

initialize_database "blewy" "/tmp/blewy.sql"

cat <<EOF > /tmp/airflow.sql
CREATE SCHEMA IF NOT EXISTS public;
GRANT ALL ON SCHEMA public TO ${POSTGRES_ROLE};
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE IF NOT EXISTS log_template (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL,
    elasticsearch_id TEXT NOT NULL,
    filename TEXT NOT NULL
);

-- Create task_instance with map_index and unique constraint
CREATE TABLE IF NOT EXISTS task_instance (
    id SERIAL PRIMARY KEY,
    task_id VARCHAR(250) NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    run_id VARCHAR(250) NOT NULL,
    map_index INTEGER NOT NULL,
    execution_date TIMESTAMPTZ,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    duration DOUBLE PRECISION,
    state VARCHAR(20),
    try_number INT,
    hostname VARCHAR(1000),
    unixname VARCHAR(1000),
    job_id INT,
    pool VARCHAR(50),
    queue VARCHAR(50),
    priority_weight INT,
    operator VARCHAR(100),
    queued_dttm TIMESTAMPTZ,
    pid INT,
    max_tries INT,
    executor_config BYTEA,
    executor VARCHAR(1000),
    params JSON,
    custom_operator_name VARCHAR(1000),
    external_executor_id VARCHAR(250),
    next_kwargs JSON,
    next_method VARCHAR(1000),
    pool_slots INT NOT NULL,
    queued_by_job_id INT,
    rendered_map_index VARCHAR(250),
    task_display_name VARCHAR(2000),
    trigger_id INT,
    trigger_timeout TIMESTAMPTZ,
    updated_at TIMESTAMPTZ,
    UNIQUE (dag_id, task_id, run_id, map_index)
);

CREATE TABLE IF NOT EXISTS task_instance_note (
    dag_id VARCHAR(250) NOT NULL,
    map_index INT NOT NULL,
    run_id VARCHAR(250) NOT NULL,
    task_id VARCHAR(250) NOT NULL,
    content VARCHAR(1000),
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    user_id INT
);

-- Create task_map with foreign key referencing task_instance
CREATE TABLE IF NOT EXISTS task_map (
    dag_id VARCHAR(250) NOT NULL, 
    task_id VARCHAR(250) NOT NULL, 
    run_id VARCHAR(250) NOT NULL, 
    map_index INTEGER NOT NULL, 
    length INTEGER NOT NULL, 
    keys JSON, 
    CONSTRAINT task_map_pkey PRIMARY KEY (dag_id, task_id, run_id, map_index), 
    CONSTRAINT ck_task_map_task_map_length_not_negative CHECK (length >= 0), 
    CONSTRAINT task_map_task_instance_fkey FOREIGN KEY(dag_id, task_id, run_id, map_index) 
        REFERENCES task_instance (dag_id, task_id, run_id, map_index) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- Create ab_permission table
CREATE TABLE IF NOT EXISTS ab_permission (
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL UNIQUE
);

-- Create ab_view_menu table
CREATE TABLE IF NOT EXISTS ab_view_menu (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Create ab_role table
CREATE TABLE IF NOT EXISTS ab_role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE
);

-- Create ab_permission_view table with permission_id and view_menu_id
CREATE TABLE IF NOT EXISTS ab_permission_view (
    id SERIAL PRIMARY KEY,
    permission_id INT NOT NULL REFERENCES ab_permission (id),
    view_menu_id INT NOT NULL REFERENCES ab_view_menu (id),
    UNIQUE (permission_id, view_menu_id)
);

-- Create ab_permission_view_role table
CREATE TABLE IF NOT EXISTS ab_permission_view_role (
    id SERIAL PRIMARY KEY,
    permission_view_id INT NOT NULL REFERENCES ab_permission_view (id),
    role_id INT NOT NULL REFERENCES ab_role (id),
    UNIQUE (permission_view_id, role_id)
);

-- Create ab_register_user table
CREATE TABLE IF NOT EXISTS ab_register_user (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128),
    registration_date TIMESTAMP,
    registration_hash VARCHAR(128)
);

-- Create ab_user table
CREATE TABLE IF NOT EXISTS ab_user (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    username VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(128),
    active BOOLEAN,
    email VARCHAR(128) NOT NULL UNIQUE,
    last_login TIMESTAMPTZ,
    login_count INT,
    fail_login_count INT,
    created_on TIMESTAMPTZ,
    changed_on TIMESTAMPTZ,
    created_by_fk INT,
    changed_by_fk INT
);

-- Create ab_user_role table
CREATE TABLE IF NOT EXISTS ab_user_role (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES ab_user (id),
    role_id INT NOT NULL REFERENCES ab_role (id),
    UNIQUE (user_id, role_id)
);

-- Create alembic_version table
CREATE TABLE IF NOT EXISTS alembic_version (
    version_num VARCHAR(32) NOT NULL,
    PRIMARY KEY (version_num)
);

-- Create session table
CREATE TABLE IF NOT EXISTS session (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(255) NOT NULL UNIQUE,
    data BYTEA,
    expiry TIMESTAMPTZ
);

-- Create serialized_dag
CREATE TABLE IF NOT EXISTS serialized_dag (
    dag_id VARCHAR(250) NOT NULL,
    dag_hash VARCHAR(32) NOT NULL,
    data JSON,
    data_compressed BYTEA,
    fileloc VARCHAR(2000) NOT NULL,
    fileloc_hash BIGINT NOT NULL,
    last_updated TIMESTAMPTZ NOT NULL,
    processor_subdir VARCHAR(2000)
);

CREATE TABLE IF NOT EXISTS callback_request (
    id SERIAL PRIMARY KEY,
    callback_data JSON NOT NULL,
    callback_type VARCHAR(20) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    priority_weight INT NOT NULL,
    processor_subdir VARCHAR(2000)
);

-- Create chart table
CREATE TABLE IF NOT EXISTS chart (
    id SERIAL PRIMARY KEY,
    chart VARCHAR(200),
    user_id INT,
    chart_url VARCHAR(2000),
    title VARCHAR(200),
    sql_layout TEXT,
    labels VARCHAR(2000),
    db VARCHAR(200),
    database_id INT,
    slices INT,
    created_on TIMESTAMPTZ,
    changed_on TIMESTAMPTZ
);

-- Create connection table
CREATE TABLE IF NOT EXISTS connection (
    id SERIAL PRIMARY KEY,
    conn_id VARCHAR(250) NOT NULL UNIQUE,
    conn_type VARCHAR(500) NOT NULL,
    description TEXT,
    host VARCHAR(500),
    schema VARCHAR(500),
    login TEXT,
    password TEXT,
    port INT,
    is_encrypted BOOLEAN,
    is_extra_encrypted BOOLEAN,
    extra TEXT
);

-- Create job table
CREATE TABLE IF NOT EXISTS job (
    id SERIAL PRIMARY KEY,
    dag_id VARCHAR(250),
    state VARCHAR(20),
    job_type VARCHAR(30),
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    latest_heartbeat TIMESTAMPTZ,
    executor_class VARCHAR(500),
    hostname VARCHAR(500),
    unixname VARCHAR(100)
);

-- Create dag table
CREATE TABLE IF NOT EXISTS dag (
    dag_id VARCHAR(250) PRIMARY KEY,
    root_dag_id VARCHAR(250),
    is_paused BOOLEAN,
    is_subdag BOOLEAN,
    is_active BOOLEAN,
    last_parsed_time TIMESTAMPTZ,
    last_scheduler_run TIMESTAMPTZ,
    last_pickled TIMESTAMPTZ,
    last_expired TIMESTAMPTZ,
    scheduler_lock TIMESTAMPTZ,
    pickle_id INT,
    fileloc VARCHAR(2000),
    processor_subdir VARCHAR(2000),
    owners VARCHAR(200),
    description TEXT,
    dag_display_name VARCHAR(250),
    default_view VARCHAR(25),
    schedule_interval VARCHAR(200),
    timetable_description TEXT,
    dataset_expression TEXT,
    max_active_tasks INT,
    max_active_runs INT,
    max_consecutive_failed_dag_runs INT,
    has_task_concurrency_limits BOOLEAN,
    concurrency INT,
    has_task_concurrency BOOLEAN,
    has_pool_concurrency BOOLEAN,
    has_complex_templated_fields BOOLEAN,
    default_args TEXT,
    tags VARCHAR(2000),
    dag_tag_list TEXT,
    has_import_errors BOOLEAN,
    next_dagrun TIMESTAMPTZ,
    next_dagrun_data_interval_start TIMESTAMPTZ,
    next_dagrun_data_interval_end TIMESTAMPTZ,
    next_dagrun_create_after TIMESTAMPTZ
);

-- Create dag_code table
CREATE TABLE IF NOT EXISTS dag_code (
    id SERIAL PRIMARY KEY,
    fileloc VARCHAR(2000) NOT NULL,
    fileloc_hash BIGINT NOT NULL,
    source_code TEXT,
    last_updated TIMESTAMPTZ,
    UNIQUE (fileloc_hash)
);

-- Create dag_pickle table
CREATE TABLE IF NOT EXISTS dag_pickle (
    id SERIAL PRIMARY KEY,
    pickle BYTEA NOT NULL,
    created_dttm TIMESTAMPTZ NOT NULL,
    pickle_hash INT
);

CREATE TABLE IF NOT EXISTS dag_priority_parsing_request (
    id VARCHAR(32) NOT NULL,
    fileloc VARCHAR(2000) NOT NULL
);

-- IMPORTANT CHANGE: conf column → BYTEA to store pickled data properly
CREATE TABLE IF NOT EXISTS dag_run (
    id SERIAL PRIMARY KEY,
    dag_id VARCHAR(250) NOT NULL,
    execution_date TIMESTAMPTZ,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    state VARCHAR(20),
    run_id VARCHAR(250) NOT NULL,
    queued_at TIMESTAMPTZ,
    creating_job_id INT,
    external_trigger BOOLEAN,
    run_type VARCHAR(20),
    conf BYTEA,  -- changed from JSON to BYTEA
    data_interval_start TIMESTAMPTZ,
    data_interval_end TIMESTAMPTZ,
    last_scheduling_decision TIMESTAMPTZ,
    dag_hash VARCHAR(32),
    log_template_id INT,
    updated_at TIMESTAMPTZ,
    clear_number INT,
    UNIQUE (dag_id, run_id),
    FOREIGN KEY (log_template_id) REFERENCES log_template (id) ON DELETE NO ACTION,
    FOREIGN KEY (creating_job_id) REFERENCES job(id)
);

CREATE TABLE IF NOT EXISTS dag_run_note (
    dag_run_id INT NOT NULL,
    content VARCHAR(1000),
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    user_id INT
);

-- Create dag_tag table
CREATE TABLE IF NOT EXISTS dag_tag (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    UNIQUE (name, dag_id)
);

CREATE TABLE IF NOT EXISTS dataset (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL,
    extra JSON NOT NULL,
    is_orphaned BOOLEAN NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    uri VARCHAR(3000) NOT NULL
);

CREATE TABLE IF NOT EXISTS dataset_alias (
    id SERIAL PRIMARY KEY,
    name VARCHAR(3000) NOT NULL
);

CREATE TABLE IF NOT EXISTS dataset_event (
    id SERIAL PRIMARY KEY,
    dataset_id INT NOT NULL,
    extra JSON NOT NULL,
    source_dag_id VARCHAR(250),
    source_map_index INT,
    source_run_id VARCHAR(250),
    source_task_id VARCHAR(250),
    timestamp TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS dataset_alias_dataset_event (
    alias_id INT NOT NULL,
    event_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS dataset_alias_dataset (
    alias_id INT NOT NULL,
    dataset_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS dag_schedule_dataset_alias_reference (
    alias_id INT NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS dagrun_dataset_event (
    data_run_id INT NOT NULL,
    event_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS dataset_dag_run_queue (
    dataset_id INT NOT NULL,
    target_dag_id VARCHAR(250) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS task_outlet_dataset_reference (
    dag_id VARCHAR(250) NOT NULL,
    dataset_id INT NOT NULL,
    task_id VARCHAR(250) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS dag_warning (
    dag_id VARCHAR(250) NOT NULL,
    warning_type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS dag_schedule_dataset_reference (
    dag_id VARCHAR(250) NOT NULL,
    dataset_id INT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS dag_owner_attributes (
    dag_id VARCHAR(250) NOT NULL,
    owner VARCHAR(500) NOT NULL,
    link VARCHAR(500) NOT NULL
);

-- Create import_error table
CREATE TABLE IF NOT EXISTS import_error (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    filename VARCHAR(512),
    stacktrace TEXT,
    processor_subdir VARCHAR(2000)
);

-- Create known_event table
CREATE TABLE IF NOT EXISTS known_event (
    id SERIAL PRIMARY KEY,
    label VARCHAR(200),
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    user_id INT,
    description TEXT
);

-- Create known_event_type table
CREATE TABLE IF NOT EXISTS known_event_type (
    id SERIAL PRIMARY KEY,
    label VARCHAR(200),
    color VARCHAR(7)
);

-- Create log table
CREATE TABLE IF NOT EXISTS log (
    id SERIAL PRIMARY KEY,
    dttm TIMESTAMPTZ NOT NULL,
    dag_id VARCHAR(250),
    task_id VARCHAR(250),
    event VARCHAR(200),
    execution_date TIMESTAMPTZ,
    owner VARCHAR(500),
    extra TEXT,
    map_index INT,
    owner_display_name VARCHAR(500),
    run_id VARCHAR(250),
    try_number INT
);

-- Create rendered_task_instance_fields table
CREATE TABLE IF NOT EXISTS rendered_task_instance_fields (
    id SERIAL PRIMARY KEY,
    dag_id VARCHAR(250) NOT NULL,
    task_id VARCHAR(250) NOT NULL,
    execution_date TIMESTAMPTZ,
    render_template_fields JSON,
    map_index INT NOT NULL,
    run_id VARCHAR(250),
    rendered_fields JSON NOT NULL,
    k8s_pod_yaml JSON
);

-- Create sensor_instance table
CREATE TABLE IF NOT EXISTS sensor_instance (
    id SERIAL PRIMARY KEY,
    dag_id VARCHAR(250) NOT NULL,
    task_id VARCHAR(250) NOT NULL,
    execution_date TIMESTAMPTZ NOT NULL,
    state VARCHAR(20),
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    duration BIGINT,
    try_number INT,
    hostname VARCHAR(500),
    unixname VARCHAR(100),
    job_id INT
);

-- Create sla_miss table
CREATE TABLE IF NOT EXISTS sla_miss (
    id SERIAL PRIMARY KEY,
    task_id VARCHAR(250),
    dag_id VARCHAR(250),
    execution_date TIMESTAMPTZ NOT NULL,
    email_sent BOOLEAN,
    timestamp TIMESTAMPTZ,
    description TEXT,
    notification_sent BOOLEAN
);

-- Create slot_pool table with include_deferred column
CREATE TABLE IF NOT EXISTS slot_pool (
    id SERIAL PRIMARY KEY,
    pool VARCHAR(50) NOT NULL,
    slots INT NOT NULL,
    description TEXT,
    include_deferred BOOLEAN DEFAULT FALSE,
    pool_hash BIGINT,
    UNIQUE (pool)
);

CREATE TABLE IF NOT EXISTS trigger (
    id SERIAL PRIMARY KEY,
    classpath VARCHAR(1000) NOT NULL,
    created_date TIMESTAMPTZ NOT NULL,
    kwargs TEXT NOT NULL,
    triggerer_id INT
);

-- Create task_fail table
CREATE TABLE IF NOT EXISTS task_fail (
    id SERIAL PRIMARY KEY,
    task_id VARCHAR(250) NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    execution_date TIMESTAMPTZ,
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL,
    duration DOUBLE PRECISION,
    map_index INT NOT NULL,
    run_id VARCHAR(250) NOT NULL
);

CREATE TABLE IF NOT EXISTS task_instance_history (
    id SERIAL PRIMARY KEY,
    custom_operator_name VARCHAR(1000),
    dag_id VARCHAR(250),
    duration DOUBLE PRECISION,
    end_date TIMESTAMPTZ NOT NULL,
    executor VARCHAR(1000),
    executor_config BYTEA,
    external_executor_id VARCHAR(250),
    hostname VARCHAR(1000),
    job_id INT,
    map_index INT NOT NULL,
    max_tries INT,
    next_kwargs JSON,
    next_method VARCHAR(1000),
    operator VARCHAR(1000),
    pid INT,
    pool VARCHAR(256) NOT NULL,
    pool_slots INT NOT NULL,
    priority_weight INT,
    queue VARCHAR(256),
    queued_by_job_id INT,
    queued_dttm TIMESTAMPTZ,
    rendered_map_index VARCHAR(250),
    run_id VARCHAR(250) NOT NULL,
    start_date TIMESTAMPTZ,
    state VARCHAR(20),
    task_display_name VARCHAR(2000),
    task_id VARCHAR(250) NOT NULL,
    trigger_id INT,
    trigger_timeout TIMESTAMPTZ,
    try_number INT NOT NULL,
    unixname VARCHAR(1000),
    updated_at TIMESTAMPTZ
);

-- Create task_reschedule table
CREATE TABLE IF NOT EXISTS task_reschedule (
    id SERIAL PRIMARY KEY,
    task_id VARCHAR(250) NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    execution_date TIMESTAMPTZ,
    start_date TIMESTAMPTZ NOT NULL,
    end_date TIMESTAMPTZ NOT NULL,
    try_number INT NOT NULL,
    reschedule_date TIMESTAMPTZ NOT NULL,
    duration INT NOT NULL,
    run_id VARCHAR(250) NOT NULL,
    map_index INT NOT NULL
);

CREATE TABLE IF NOT EXISTS variable (
    id SERIAL PRIMARY KEY,
    description TEXT,
    key VARCHAR(250) NOT NULL UNIQUE,
    val VARCHAR(2000),
    is_encrypted BOOLEAN
);

CREATE TABLE IF NOT EXISTS xcom (
    id SERIAL PRIMARY KEY,
    key VARCHAR(512) NOT NULL,
    value BYTEA,
    timestamp TIMESTAMPTZ,
    execution_date TIMESTAMPTZ,
    task_id VARCHAR(250) NOT NULL,
    dag_id VARCHAR(250) NOT NULL,
    dag_run_id INT NOT NULL,
    map_index INT NOT NULL,
    run_id VARCHAR(250)
);

-- Grant privileges on all tables and sequences
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${POSTGRES_ROLE};
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${POSTGRES_ROLE};

-- Grant usage and select/update on all sequences
DO \$\$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = 'public') LOOP
        EXECUTE 'GRANT USAGE, SELECT, UPDATE ON SEQUENCE ' || quote_ident(r.sequence_name) || ' TO ${POSTGRES_ROLE};';
    END LOOP;
END \$\$;

-- Grant execute on all functions
DO \$\$ 
DECLARE 
    r RECORD;
BEGIN
    FOR r IN (SELECT routine_name FROM information_schema.routines WHERE routine_schema = 'public') LOOP
        EXECUTE 'GRANT EXECUTE ON FUNCTION ' || quote_ident(r.routine_name) || ' TO ${POSTGRES_ROLE};';
    END LOOP;
END \$\$;
EOF

initialize_database "airflow" "/tmp/airflow.sql"

echo "All databases have been initialized successfully."
