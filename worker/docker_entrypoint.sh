#!/bin/bash

echo "Attempting to connect to kafka broker at ${KAFKA_HOST}:${KAFKA_PORT}"
while nc -z "${KAFKA_HOST}" "${KAFKA_PORT}"; ret=$?; [ "${ret}" -ne 0 ]; do
  echo "kafka broker is unavailable - sleeping..."
  sleep 1
done
  echo "kafka broker connection established."

echo "Attempting to connect to influxdb at ${INFLUXDB_HOST}:${INFLUXDB_PORT}"
while nc -z "${INFLUXDB_HOST}" "${INFLUXDB_PORT}"; ret=$?; [ "${ret}" -ne 0 ]; do
  echo "influxdb is unavailable - sleeping..."
  sleep 1
done
  echo "influxdb connection established."

echo "Starting worker..."
python ./main.py
exit
