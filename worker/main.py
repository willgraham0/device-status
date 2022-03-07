import os

from influxdb_client import InfluxDBClient, Point
from kafka import KafkaConsumer


influxdb_host = os.environ['INFLUXDB_HOST']
influxdb_port = os.environ['INFLUXDB_PORT']
influxdb_org = os.environ["INFLUXDB_ORG"]
influxdb_token = os.environ["INFLUXDB_TOKEN"]
influxdb_bucket = os.environ["INFLUXDB_BUCKET"]
kafka_host = os.environ["KAFKA_HOST"]
kafka_port = os.environ["KAFKA_PORT"]
kafka_topic = os.environ["KAFKA_TOPIC"]

influxdb_client = InfluxDBClient(url=f"http://{influxdb_host}:{influxdb_port}", org=influxdb_org, token=influxdb_token)
kafka_consumer = KafkaConsumer(kafka_topic, bootstrap_servers=f"{kafka_host}:{kafka_port}")


def run_loop():
    with influxdb_client.write_api() as write_api:
        for record in kafka_consumer:
            device = record.key.decode("utf-8")
            point = Point(kafka_topic).field(device, 1)
            write_api.write(bucket=influxdb_bucket, record=point)


if __name__ == "__main__":
    run_loop()
