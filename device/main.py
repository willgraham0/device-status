import json
import os
import random

from kafka import KafkaProducer


device_name = os.environ["NAME"]
kafka_host = os.environ["KAFKA_HOST"]
kafka_port = os.environ["KAFKA_PORT"]
kafka_topic = os.environ["KAFKA_TOPIC"]


def publish_status():
    kafka_producer = KafkaProducer(bootstrap_servers=f"{kafka_host}:{kafka_port}")
    kafka_producer.send(
        kafka_topic,
        value=bytes(json.dumps({"power": random.randint(0, 100), "other": "ACK"}), "utf-8"),
        key=bytes(device_name, "utf-8"),
    )


if __name__ == "__main__":
    publish_status()
