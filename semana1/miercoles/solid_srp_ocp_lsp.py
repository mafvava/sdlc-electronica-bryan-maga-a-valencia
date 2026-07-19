from dataclasses import dataclass
from typing import Protocol


# ============================================================
# SRP - Single Responsibility Principle
# ============================================================


# ❌ EJEMPLO INCORRECTO
class BadPressureSensor:
    """
    Esta clase viola SRP porque tiene demasiadas responsabilidades:
    leer el sensor, validar la lectura y guardarla.
    """

    def read(self) -> float:
        """Simula la lectura de presión."""
        return 2.5

    def validate(self, pressure: float) -> bool:
        """Valida que la presión sea positiva."""
        return pressure >= 0

    def save(self, pressure: float) -> None:
        """Simula guardar la lectura."""
        print(f"Guardando presión: {pressure} bar")


# ✅ EJEMPLO CORRECTO
class PressureSensor:
    """Responsable únicamente de obtener lecturas de presión."""

    def read(self) -> float:
        """Simula la lectura de presión."""
        return 2.5


class PressureValidator:
    """Responsable únicamente de validar lecturas."""

    def is_valid(self, pressure: float) -> bool:
        """Determina si una presión es válida."""
        return pressure >= 0


class PressureRepository:
    """Responsable únicamente de persistir lecturas."""

    def save(self, pressure: float) -> None:
        """Simula guardar una lectura."""
        print(f"Guardando presión: {pressure} bar")


# ============================================================
# OCP - Open/Closed Principle
# ============================================================


# ❌ EJEMPLO INCORRECTO
class BadPressureAlarm:
    """
    Esta clase viola OCP porque debemos modificarla cada vez
    que queremos agregar un nuevo tipo de alarma.
    """

    def check(self, pressure: float, alarm_type: str) -> bool:
        """Comprueba una condición de alarma."""
        if alarm_type == "high":
            return pressure > 10

        if alarm_type == "low":
            return pressure < 1

        return False


# ✅ EJEMPLO CORRECTO
class PressureRule(Protocol):
    """Define el contrato para una regla de presión."""

    def check(self, pressure: float) -> bool:
        """Comprueba si se cumple una condición."""
        ...


class HighPressureRule:
    """Detecta presiones superiores al límite."""

    def __init__(self, limit: float) -> None:
        self.limit = limit

    def check(self, pressure: float) -> bool:
        """Devuelve True si la presión supera el límite."""
        return pressure > self.limit


class LowPressureRule:
    """Detecta presiones inferiores al límite."""

    def __init__(self, limit: float) -> None:
        self.limit = limit

    def check(self, pressure: float) -> bool:
        """Devuelve True si la presión está por debajo del límite."""
        return pressure < self.limit


class PressureAlarm:
    """Evalúa una presión utilizando una regla configurable."""

    def __init__(self, rule: PressureRule) -> None:
        self.rule = rule

    def check(self, pressure: float) -> bool:
        """Comprueba si se activa la alarma."""
        return self.rule.check(pressure)


# ============================================================
# LSP - Liskov Substitution Principle
# ============================================================


@dataclass
class PressureReading:
    """Representa una lectura de presión."""

    value: float
    unit: str


# ❌ EJEMPLO INCORRECTO
class BadPressureSensorBase:
    """Clase base utilizada para demostrar una violación de LSP."""

    def read(self) -> PressureReading:
        """Devuelve una lectura de presión."""
        return PressureReading(value=2.5, unit="bar")


class BadOfflineSensor(BadPressureSensorBase):
    """
    Viola LSP porque cambia el comportamiento esperado de read()
    lanzando una excepción en lugar de devolver una lectura.
    """

    def read(self) -> PressureReading:
        """Simula un sensor fuera de línea."""
        raise RuntimeError("Sensor fuera de línea")


# ✅ EJEMPLO CORRECTO
class PressureReader(Protocol):
    """Contrato para cualquier fuente válida de lecturas."""

    def read(self) -> PressureReading:
        """Obtiene una lectura de presión."""
        ...


class IndustrialPressureSensor:
    """Sensor industrial que proporciona lecturas de presión."""

    def read(self) -> PressureReading:
        """Devuelve una lectura válida."""
        return PressureReading(value=2.5, unit="bar")


class SimulatedPressureSensor:
    """Sensor simulado compatible con el mismo contrato."""

    def read(self) -> PressureReading:
        """Devuelve una lectura simulada."""
        return PressureReading(value=2.5, unit="bar")


def process_pressure_sensor(sensor: PressureReader) -> PressureReading:
    """
    Procesa cualquier sensor que cumpla el contrato PressureReader.
    """

    return sensor.read()