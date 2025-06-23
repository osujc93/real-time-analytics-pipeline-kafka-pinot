#!/usr/bin/env bash
#
# start-pinot-controller.sh
# Starts the Pinot Controller in the background, then adds tables,
# then waits to keep the container running.

# 1) Start the Pinot Controller in the background:
StartController \
  -configFileName /opt/pinot/conf/pinot-controller.conf \
  -clusterName pinot-cluster \
  -zkAddress zookeeper1:2181,zookeeper2:2181,zookeeper3:2181,zookeeper4:2181,zookeeper5:2181 \
  -controllerHost pinot-controller \
  -controllerPort 9000 &

# 2) Wait for the controller to start up (simple sleep; can adjust as needed)
sleep 10

# 3) Add the clickstreams table
/opt/pinot/bin/pinot-admin.sh AddTable \
  -schemaFile /opt/pinot/conf/clickstreams/schema.json \
  -tableConfigFile /opt/pinot/conf/clickstreams/table.json \
  -controllerHost 127.0.0.1 \
  -controllerPort 9000 \
  -exec

# 4) Add the orders table
/opt/pinot/bin/pinot-admin.sh AddTable \
  -schemaFile /opt/pinot/conf/orders/schema.json \
  -tableConfigFile /opt/pinot/conf/orders/table.json \
  -controllerHost 127.0.0.1 \
  -controllerPort 9000 \
  -exec

# 5) Keep container running by waiting on the background StartController process:
wait
