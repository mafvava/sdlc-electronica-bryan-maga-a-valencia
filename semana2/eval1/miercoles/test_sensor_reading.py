from datetime import datetime, timezone

import pytest

from semana2.eval1.miercoles.sensor_reading import SensorReading


def test_sensor_reading_is_created_correctly() -> None:
    timestamp = datetime.now(timezone.utc)

    reading = SensorReading(
        sensor_id="sensor-01",
        temperature=25.5,
        humidity=60.0,
        timestamp=timestamp,
    )

    assert reading.sensor_id == "sensor-01"
    assert reading.temperature == 25.5
    assert reading.humidity == 60.0
    assert reading.timestamp == timestamp


def test_sensor_reading_rejects_empty_sensor_id() -> None:
    with pytest.raises(ValueError):
        SensorReading(
            sensor_id="",
            temperature=25.0,
            humidity=60.0,
            timestamp=datetime.now(timezone.utc),
        )


def test_sensor_reading_rejects_invalid_humidity() -> None:
    with pytest.raises(ValueError):
        SensorReading(
            sensor_id="sensor-01",
            temperature=25.0,
            humidity=101.0,
            timestamp=datetime.now(timezone.utc),
        )


def test_sensor_reading_rejects_invalid_temperature() -> None:
    with pytest.raises(ValueError):
        SensorReading(
            sensor_id="sensor-01",
            temperature=150.0,
            humidity=60.0,
            timestamp=datetime.now(timezone.utc),
        )


def test_sensor_reading_is_immutable() -> None:
    reading = SensorReading(
        sensor_id="sensor-01",
        temperature=25.0,
        humidity=60.0,
        timestamp=datetime.now(timezone.utc),
    )

    with pytest.raises((AttributeError, TypeError)):
        reading.temperature = 30.0  # type: ignore[misc]