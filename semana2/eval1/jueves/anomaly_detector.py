from dataclasses import dataclass

from semana2.eval1.miercoles.sensor_reading import SensorReading


@dataclass(frozen=True)
class AnomalyThresholds:
    """Define los límites que usamos para detectar anomalías."""

    max_temperature: float
    max_humidity: float


class AnomalyDetector:
    """Detecta anomalías usando umbrales que recibe desde afuera."""

    def __init__(self, thresholds: AnomalyThresholds) -> None:
        self._thresholds = thresholds

    def is_anomalous(self, reading: SensorReading) -> bool:
        # Si cualquiera de los dos valores supera su límite, hay anomalía.
        return (
            reading.temperature > self._thresholds.max_temperature
            or reading.humidity > self._thresholds.max_humidity
        )

    def reasons(self, reading: SensorReading) -> list[str]:
        # Guardamos las razones para saber exactamente qué pasó.
        reasons: list[str] = []

        if reading.temperature > self._thresholds.max_temperature:
            reasons.append("temperature")

        if reading.humidity > self._thresholds.max_humidity:
            reasons.append("humidity")

        return reasons