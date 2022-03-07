FROM python:3.8.1-slim

ENV NAME=${NAME}
ENV PERIOD=${PERIOD}
ENV KAFKA_HOST=${KAFKA_HOST}
ENV KAFKA_PORT=${KAFKA_PORT}
ENV KAFKA_TOPIC=${KAFKA_TOPIC}

RUN apt-get update && apt-get -y install netcat

WORKDIR /usr/device
COPY . .

RUN chmod +x ./docker_entrypoint.sh

RUN useradd -ms /bin/bash device
USER device

ENV PATH $PATH:/home/device/.local/bin

RUN pip install --no-cache-dir --disable-pip-version-check --user -r requirements.txt
ENTRYPOINT ["./docker_entrypoint.sh"]
