from datetime import datetime

import pytest

from semana1.lunes.reading import (
    Reading,
    SensorStatus,
    SensorType,
    convert_bar_to_psi,
    convert_psi_to_bar,
    is_alarm_condition,
    is_valid_reading,
    normalize_pressure,
)


@pytest.fixture
def pressure_reading() -> Reading:
    """Crea una lectura de presión de prueba."""
    return Reading(
        sensor_id="PRESS-001",
        sensor_type=SensorType.PRESSURE,
        value=2.5,
        unit="bar",
        timestamp=datetime(2026, 7, 13, 12, 0, 0),
        status=SensorStatus.OK,
    )


def test_reading_is_created_correctly(pressure_reading: Reading) -> None:
    """Verifica que una lectura se cree correctamente."""
    assert pressure_reading.sensor_id == "PRESS-001"
    assert pressure_reading.sensor_type is SensorType.PRESSURE
    assert pressure_reading.value == 2.5
    assert pressure_reading.unit == "bar"
    assert pressure_reading.status is SensorStatus.OK


def test_reading_is_immutable(pressure_reading: Reading) -> None:
    """Verifica que Reading sea inmutable."""
    with pytest.raises(AttributeError):
        pressure_reading.value = 5.0  # type: ignore[misc]


def test_valid_reading(pressure_reading: Reading) -> None:
    """Verifica que una lectura válida sea aceptada."""
    assert is_valid_reading(pressure_reading) is True


def test_invalid_negative_reading(pressure_reading: Reading) -> None:
    """Verifica que una presión negativa sea inválida."""
    invalid_reading = Reading(
        sensor_id=pressure_reading.sensor_id,
        sensor_type=pressure_reading.sensor_type,
        value=-1.0,
        unit="bar",
        timestamp=pressure_reading.timestamp,
        status=pressure_reading.status,
    )

    assert is_valid_reading(invalid_reading) is False


def test_offline_reading_is_invalid(pressure_reading: Reading) -> None:
    """Verifica que un sensor offline produzca una lectura inválida."""
    offline_reading = Reading(
        sensor_id=pressure_reading.sensor_id,
        sensor_type=pressure_reading.sensor_type,
        value=2.5,
        unit="bar",
        timestamp=pressure_reading.timestamp,
        status=SensorStatus.OFFLINE,
    )

    assert is_valid_reading(offline_reading) is False


def test_convert_bar_to_psi(pressure_reading: Reading) -> None:
    """Verifica la conversión de bar a psi."""
    converted = convert_bar_to_psi(pressure_reading)

    assert converted.unit == "psi"
    assert converted.value == pytest.approx(36.2595, rel=1e-4)


def test_convert_psi_to_bar() -> None:
    """Verifica la conversión de psi a bar."""
    reading = Reading(
        sensor_id="PRESS-002",
        sensor_type=SensorType.PRESSURE,
        value=14.5038,
        unit="psi",
        timestamp=datetime(2026, 7, 13, 12, 0, 0),
        status=SensorStatus.OK,
    )

    converted = convert_psi_to_bar(reading)

    assert converted.unit == "bar"
    assert converted.value == pytest.approx(1.0, rel=1e-4)


def test_pressure_alarm(pressure_reading: Reading) -> None:
    """Verifica la detección de una condición de alarma."""
    assert is_alarm_condition(pressure_reading, 2.0) is True
    assert is_alarm_condition(pressure_reading, 3.0) is False


def test_normalize_pressure(pressure_reading: Reading) -> None:
    """Verifica la normalización de una lectura a bar."""
    normalized = normalize_pressure(pressure_reading)

    assert normalized.unit == "bar"
    assert normalized.value == pressure_reading.value


def test_normalize_psi_to_bar() -> None:
    """Verifica que normalize_pressure convierta psi a bar."""
    reading = Reading(
        sensor_id="PRESS-003",
        sensor_type=SensorType.PRESSURE,
        value=14.5038,
        unit="psi",
        timestamp=datetime(2026, 7, 13, 12, 0, 0),
        status=SensorStatus.OK,
    )

    normalized = normalize_pressure(reading)

    assert normalized.unit == "bar"
    assert normalized.value == pytest.approx(1.0, rel=1e-4)