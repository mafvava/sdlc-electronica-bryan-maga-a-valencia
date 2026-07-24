from datetime import datetime, timezone

from semana2.eval1.jueves.anomaly_detector import (
    AnomalyDetector,
    AnomalyThresholds,
)
from semana2.eval1.miercoles.sensor_reading import SensorReading


def create_reading(
    temperature: float,
    humidity: float,
) -> SensorReading:
    return SensorReading(
        sensor_id="sensor-01",
        temperature=temperature,
        humidity=humidity,
        timestamp=datetime.now(timezone.utc),
    )


def test_temperature_above_threshold_is_anomaly() -> None:
    detector = AnomalyDetector(
        AnomalyThresholds(
            max_temperature=35.0,
            max_humidity=80.0,
        )
    )

    reading = create_reading(36.0, 60.0)

    assert detector.is_anomalous(reading) is True
    assert detector.reasons(reading) == ["temperature"]


def test_humidity_above_threshold_is_anomaly() -> None:
    detector = AnomalyDetector(
        AnomalyThresholds(
            max_temperature=35.0,
            max_humidity=80.0,
        )
    )

    reading = create_reading(25.0, 85.0)

    assert detector.is_anomalous(reading) is True
    assert detector.reasons(reading) == ["humidity"]


def test_normal_reading_is_not_anomaly() -> None:
    detector = AnomalyDetector(
        AnomalyThresholds(
            max_temperature=35.0,
            max_humidity=80.0,
        )
    )

    reading = create_reading(25.0, 60.0)

    assert detector.is_anomalous(reading) is False
    assert detector.reasons(reading) == []


def test_detector_uses_injected_thresholds() -> None:
    detector = AnomalyDetector(
        AnomalyThresholds(
            max_temperature=30.0,
            max_humidity=70.0,
        )
    )

    reading = create_reading(31.0, 60.0)

    assert detector.is_anomalous(reading) is True
    assert detector.reasons(reading) == ["temperature"]