"""Application metrics collector for InfluxDB."""
import os
import time

INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "")
INFLUX_ORG = os.getenv("INFLUX_ORG", "beehive")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET", "sensors")


def record_api_request(endpoint: str, duration_ms: float, status_code: int) -> None:
    """Write API request metric to InfluxDB."""
    try:
        from influxdb_client import InfluxDBClient, Point
        from influxdb_client.client.write_api import SYNCHRONOUS

        client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = (
            Point("api_request")
            .tag("endpoint", endpoint)
            .tag("status", str(status_code))
            .field("duration_ms", duration_ms)
            .time(time.time_ns())
        )
        write_api.write(bucket=INFLUX_BUCKET, record=point)
    except Exception:
        pass


def record_sensor_data(beehive_id: int, temperature: float, humidity: float, weight: float) -> None:
    """Write sensor reading to InfluxDB."""
    try:
        from influxdb_client import InfluxDBClient, Point
        from influxdb_client.client.write_api import SYNCHRONOUS

        client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = (
            Point("sensor_reading")
            .tag("beehive_id", str(beehive_id))
            .field("temperature", temperature)
            .field("humidity", humidity)
            .field("weight", weight)
            .time(time.time_ns())
        )
        write_api.write(bucket=INFLUX_BUCKET, record=point)
    except Exception:
        pass
