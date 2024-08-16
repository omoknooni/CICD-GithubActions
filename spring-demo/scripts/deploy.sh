#!/bin/bash
BUILD_JAR=$(ls /home/ubuntu/spring-demo/*.jar)
$JAR_NAME=$(basename $BUILD_JAR)
echo "[*] JAR Path: $BUILD_JAR"
chmod +x $BUILD_JAR

CURRENT_PID=$(pgrep -f $JAR_NAME)
if [ -z $CURRENT_PID ]; then
  echo "no process"
else
  echo "kill $CURRENT_PID"
  kill -9 $CURRENT_PID
  echo "[*] $CURRENT_PID kill success"
  sleep 5
fi

nohup java -jar $BUILD_JAR >> /home/ubuntu/spring-demo/deploy.log 2>> /home/ubuntu/spring-demo/deploy_err.log &
echo "[*] $JAR_NAME deploy success"