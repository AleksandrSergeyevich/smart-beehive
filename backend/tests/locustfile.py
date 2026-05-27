"""Locust load test for Smart Beehive API."""
from locust import HttpUser, between, task


class BeehiveAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_sensor_data(self):
        self.client.get("/api/v1/beehives/")

    @task(2)
    def get_beehive_status(self):
        self.client.get("/api/v1/beehives/1/status")

    @task(2)
    def get_sensor_latest(self):
        self.client.get("/api/v1/sensors/1/latest")

    @task(1)
    def get_ml_prediction(self):
        self.client.get("/api/v1/beehives/1/prediction")

    @task(1)
    def health_check(self):
        self.client.get("/health")
