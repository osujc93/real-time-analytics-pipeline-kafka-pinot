#!/bin/bash

echo "$(date '+%Y-%m-%d %H:%M:%S') - Start-Zookeeper-Script Has Started..."

sudo chown -R zookeeper5:zookeeper /data /logs /datalog /conf/ssl

# Logging (optional)
LOG_FILE="/logs/start_zookeeper.log"
exec > >(tee -a "$LOG_FILE") 2>&1

# Set Java environment
export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
export PATH="$JAVA_HOME/bin:$PATH"
export ZK_NODE_ID=5

echo "5" > /data/myid

# Ports used by ZooKeeper
client_port=2181
secure_client_port=2281
admin_port=7071
quorum_ports="2888 3888"
port4=7001

# Function to stop processes using a specific port
stop_process_using_port() {
    port=$1
    process_pid=$(lsof -ti tcp:$port)
    if [ -n "$process_pid" ]; then
        echo "Port $port is in use by process $process_pid. Stopping process..."
        kill -9 $process_pid
        echo "Process $process_pid stopped."
    else
        echo "Port $port is not in use."
    fi
}

# Check and stop processes using ZooKeeper ports
stop_process_using_port $client_port
stop_process_using_port $secure_client_port
stop_process_using_port $admin_port
stop_process_using_port $port4
stop_process_using_port $quorum_ports
for port in $quorum_ports; do
    stop_process_using_port $port
done

# Ensure the keytab files are in the new ext4 directory
KEYTAB_EXT4_DIR="/conf/zookeeper_keytabs"

# Create the new directory on the ext4 filesystem if it doesn't exist
if [ ! -d "$KEYTAB_EXT4_DIR" ]; then
    sudo mkdir -p "$KEYTAB_EXT4_DIR"
    sudo chown -R zookeeper5:zookeeper "$KEYTAB_EXT4_DIR"
fi

# Move keytabs to the ext4 filesystem directory and ensure proper permissions
if [ ! -f ${KEYTAB_EXT4_DIR}/zookeeper-server5.keytab ]; then
    sudo cp /etc/krb5kdc/keytabs/zookeeper-server5.keytab ${KEYTAB_EXT4_DIR}/zookeeper-server5.keytab
fi
sudo chown zookeeper5:zookeeper ${KEYTAB_EXT4_DIR}/zookeeper-server5.keytab
sudo chmod 640 ${KEYTAB_EXT4_DIR}/zookeeper-server5.keytab

if [ ! -f ${KEYTAB_EXT4_DIR}/zookeeper-quorum5.keytab ]; then
    sudo cp /etc/krb5kdc/keytabs/zookeeper-quorum5.keytab ${KEYTAB_EXT4_DIR}/zookeeper-quorum5.keytab
fi
sudo chown zookeeper5:zookeeper ${KEYTAB_EXT4_DIR}/zookeeper-quorum5.keytab
sudo chmod 640 ${KEYTAB_EXT4_DIR}/zookeeper-quorum5.keytab

if [ ! -f ${KEYTAB_EXT4_DIR}/zookeeper-quorum-client5.keytab ]; then
    sudo cp /etc/krb5kdc/keytabs/zookeeper-quorum-client5.keytab ${KEYTAB_EXT4_DIR}/zookeeper-quorum-client5.keytab
fi
sudo chown zookeeper5:zookeeper ${KEYTAB_EXT4_DIR}/zookeeper-quorum-client5.keytab
sudo chmod 640 ${KEYTAB_EXT4_DIR}/zookeeper-quorum-client5.keytab

# Compile BouncyCastle Jar

sudo /apache-zookeeper-3.8.4-bin/bin/setup_bouncycastle_agent.sh

sudo chown zookeeper5:zookeeper /apache-zookeeper-3.8.4-bin/lib/BouncyCastleAgent-fat.jar

sudo chmod 640 /apache-zookeeper-3.8.4-bin/lib/BouncyCastleAgent-fat.jar

# Stop Zookeeper if running and restart in the foreground
if pgrep -x "zookeeper" > /dev/null; then
    echo "Zookeeper is running, stopping it now..."
    /apache-zookeeper-3.8.4-bin/bin/zkServer.sh stop
    sleep 10
fi

# Step 3: Start Zookeeper without SASL/TLS
echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting Zookeeper without SASL/TLS..."
/apache-zookeeper-3.8.4-bin/bin/zkServer.sh start-foreground

# Give Zookeeper time to start
sleep 60

echo "$(date '+%Y-%m-%d %H:%M:%S') - Zookeeper script completed successfully."
