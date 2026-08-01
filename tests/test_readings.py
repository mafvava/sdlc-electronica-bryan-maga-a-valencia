import uuid
from datetime import datetime, timedelta
from typing import cast

from fastapi.testclient import TestClient


def create_sensor(client: TestClient) -> int:
    response = client.post(
        "/sensors/",
        json={
            "name": f"Sensor-{uuid.uuid4()}",
            "sensor_type": "temperature",
            "unit": "C",
            "location": "Laboratorio",
        },
    )

    return cast(int, response.json()["id"])


def test_create_reading(client: TestClient):
    sensor_id = create_sensor(client)

    response = client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 25.5,
            "timestamp": (
                datetime.now().isoformat()
            ),
        },
    )

    assert response.status_code == 201
    assert response.json()["value"] == 25.5


def test_get_all_readings(client: TestClient):
    sensor_id = create_sensor(client)

    client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 21,
            "timestamp": (
                datetime.now().isoformat()
            ),
        },
    )

    response = client.get("/readings/")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_reading_by_id(client: TestClient):
    sensor_id = create_sensor(client)

    created = client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 28,
            "timestamp": (
                datetime.now().isoformat()
            ),
        },
    )

    reading_id = created.json()["id"]

    response = client.get(
        f"/readings/{reading_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == reading_id


def test_delete_reading(client: TestClient):
    sensor_id = create_sensor(client)

    created = client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 30,
            "timestamp": (
                datetime.now().isoformat()
            ),
        },
    )

    reading_id = created.json()["id"]

    response = client.delete(
        f"/readings/{reading_id}"
    )

    assert response.status_code == 204


def test_filter_by_date(client: TestClient):
    sensor_id = create_sensor(client)

    now = datetime.now()

    client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 24,
            "timestamp": now.isoformat(),
        },
    )

    start = (
        now - timedelta(minutes=1)
    ).isoformat()

    end = (
        now + timedelta(minutes=1)
    ).isoformat()

    response = client.get(
        "/readings/filter/date"
        f"?start={start}&end={end}"
    )

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_temperature_out_of_range(
    client: TestClient,
):
    sensor_id = create_sensor(client)

    response = client.post(
        "/readings/",
        json={
            "sensor_id": sensor_id,
            "value": 500,
            "timestamp": (
                datetime.now().isoformat()
            ),
        },
    )

    assert response.status_code == 422