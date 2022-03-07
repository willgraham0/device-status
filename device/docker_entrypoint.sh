#!/bin/bash

echo "Attempting to connect to kafka broker at ${KAFKA_HOST}:${KAFKA_PORT}"
while nc -z "${KAFKA_HOST}" "${KAFKA_PORT}"; ret=$?; [ "${ret}" -ne 0 ]; do
  echo "kafka broker is unavailable - sleeping..."
  sleep 1
done
  echo "kafka broker connection established."

echo "Starting ${NAME}..."
while true
do
  python ./main.py
  sleep "${PERIOD}"
done
exit
