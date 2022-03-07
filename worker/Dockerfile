FROM python:3.8.1-slim

ENV INFLUXDB_HOST=${INFLUXDB_HOST}
ENV INFLUXDB_PORT=${INFLUXDB_PORT}
ENV INFLUXDB_TOKEN=${INFLUXDB_TOKEN}
ENV INFLUXDB_ORG=${INFLUXDB_ORG}
ENV INFLUXDB_BUCKET=${INFLUXDB_BUCKET}
ENV KAFKA_HOST=${KAFKA_HOST}
ENV KAFKA_PORT=${KAFKA_PORT}
ENV KAFKA_TOPIC=${KAFKA_TOPIC}

RUN apt-get update && apt-get -y install netcat

WORKDIR /usr/worker
COPY . .

RUN chmod +x ./docker_entrypoint.sh

RUN useradd -ms /bin/bash worker
USER worker

ENV PATH $PATH:/home/worker/.local/bin

RUN pip install --no-cache-dir --disable-pip-version-check --user -r requirements.txt
ENTRYPOINT ["./docker_entrypoint.sh"]
