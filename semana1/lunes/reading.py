from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Protocol


class SensorStatus(Enum):
    """Representa el estado operativo de un sensor."""

    OK = auto()
    WARNING = auto()
    ERROR = auto()
    OFFLINE = auto()


class SensorType(Enum):
    """Tipos de sensores soportados por el sistema."""

    PRESSURE = auto()
    TEMPERATURE = auto()
    FLOW = auto()
    LEVEL = auto()


@dataclass(frozen=True)
class Reading:
    """Representa una lectura realizada por un sensor."""

    sensor_id: str
    sensor_type: SensorType
    value: float
    unit: str
    timestamp: datetime
    status: SensorStatus


class Sensor(Protocol):
    """Interfaz que debe implementar cualquier sensor."""

    def read(self) -> Reading:
        """Obtiene una lectura del sensor."""
        ...


def is_valid_reading(reading: Reading) -> bool:
    """Determina si una lectura de presión es válida."""
    return (
        reading.value >= 0
        and reading.unit.lower() in {"bar", "psi", "kpa", "mpa"}
        and reading.status != SensorStatus.OFFLINE
    )


def convert_bar_to_psi(reading: Reading) -> Reading:
    """Convierte una lectura de presión de bar a psi."""
    if reading.unit.lower() != "bar":
        raise ValueError("La lectura debe estar expresada en bar.")

    return Reading(
        sensor_id=reading.sensor_id,
        sensor_type=reading.sensor_type,
        value=reading.value * 14.5038,
        unit="psi",
        timestamp=reading.timestamp,
        status=reading.status,
    )


def convert_psi_to_bar(reading: Reading) -> Reading:
    """Convierte una lectura de presión de psi a bar."""
    if reading.unit.lower() != "psi":
        raise ValueError("La lectura debe estar expresada en psi.")

    return Reading(
        sensor_id=reading.sensor_id,
        sensor_type=reading.sensor_type,
        value=reading.value / 14.5038,
        unit="bar",
        timestamp=reading.timestamp,
        status=reading.status,
    )


def is_alarm_condition(reading: Reading, maximum_pressure: float) -> bool:
    """Determina si la presión supera el límite máximo permitido."""
    return reading.value > maximum_pressure


def normalize_pressure(reading: Reading) -> Reading:
    """Devuelve una nueva lectura de presión expresada en bar."""
    if reading.unit.lower() == "bar":
        return reading

    if reading.unit.lower() == "psi":
        return convert_psi_to_bar(reading)

    raise ValueError("Unidad de presión no soportada.")