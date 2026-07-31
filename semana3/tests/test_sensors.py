from fastapi.testclient import TestClient


def test_create_sensor(client: TestClient):
    response = client.post(
        "/sensors/",
        json={
            "name": "Sensor Temperatura",
            "sensor_type": "temperature",
            "unit": "°C",
            "location": "Bodega Norte",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Sensor Temperatura"
    assert data["sensor_type"] == "temperature"
    assert data["unit"] == "°C"
    assert data["location"] == "Bodega Norte"
    assert "id" in data


def test_get_all_sensors(client: TestClient):
    response = client.get("/sensors/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_sensor_by_id(client: TestClient):
    create = client.post(
        "/sensors/",
        json={
            "name": "Sensor Humedad",
            "sensor_type": "humidity",
            "unit": "%",
            "location": "Bodega Sur",
        },
    )

    sensor_id = create.json()["id"]

    response = client.get(f"/sensors/{sensor_id}")

    assert response.status_code == 200
    assert response.json()["id"] == sensor_id


def test_update_sensor(client: TestClient):
    create = client.post(
        "/sensors/",
        json={
            "name": "Sensor Viejo",
            "sensor_type": "temperature",
            "unit": "°C",
            "location": "Zona A",
        },
    )

    sensor_id = create.json()["id"]

    response = client.put(
        f"/sensors/{sensor_id}",
        json={
            "name": "Sensor Nuevo",
            "sensor_type": "temperature",
            "unit": "°C",
            "location": "Zona B",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Sensor Nuevo"
    assert data["location"] == "Zona B"


def test_delete_sensor(client: TestClient):
    create = client.post(
        "/sensors/",
        json={
            "name": "Sensor Eliminar",
            "sensor_type": "temperature",
            "unit": "°C",
            "location": "Temporal",
        },
    )

    sensor_id = create.json()["id"]

    response = client.delete(f"/sensors/{sensor_id}")

    assert response.status_code == 204

    response = client.get(f"/sensors/{sensor_id}")

    assert response.status_code == 404


def test_duplicate_sensor(client: TestClient):
    sensor = {
        "name": "Sensor Duplicado",
        "sensor_type": "temperature",
        "unit": "°C",
        "location": "Laboratorio",
    }

    first_response = client.post(
        "/sensors/",
        json=sensor,
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/sensors/",
        json=sensor,
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == (
        "Ya existe un sensor con ese nombre."
    )