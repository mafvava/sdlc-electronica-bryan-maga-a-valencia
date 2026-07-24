from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SensorReading:
    """Representa una lectura de temperatura y humedad de un sensor."""

    sensor_id: str
    temperature: float
    humidity: float
    timestamp: datetime

    def __post_init__(self) -> None:
        # Aquí validamos que los datos básicos tengan sentido.
        if not self.sensor_id.strip():
            raise ValueError("El sensor_id no puede estar vacío.")

        if self.temperature < -50 or self.temperature > 100:
            raise ValueError("La temperatura está fuera de rango.")

        if self.humidity < 0 or self.humidity > 100:
            raise ValueError("La humedad debe estar entre 0 y 100.")