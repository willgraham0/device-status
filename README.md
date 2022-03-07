# Device Status

## Introduction

We want to visualise the time at when each of our IoT devices
submits some data.

## Architecture

Each device publishes data to a Kafka topic on some time interval.
A worker subscribes to this topic and consumes the data, saving it 
to an InfluxDB timeseries database. Grafana connects to this datasource
to visualise the data.

The architecture is laid out below:

![alt text][architecture]

## Usage

To spin up the services enter the following command:

```bash
docker-compose up
```

Then go to `localhost:3000` to use Grafana to visualise the data.

![alt text][dashboard]


[architecture]: docs/device-status-architecture.png "architecture"
[dashboard]: docs/device-status-dashboard.png "dashboard"
