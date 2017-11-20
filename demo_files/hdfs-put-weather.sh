#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "Error: usage ./hdfs-put-weather.sh <path>"
    exit -1
fi

HDFS_DIR=/user/vagrant/$1

echo "Uploading files to $HDFS_DIR"

hdfs dfs -rm $HDFS_DIR/*.txt
hdfs dfs -put ./weather_*.txt $HDFS_DIR
