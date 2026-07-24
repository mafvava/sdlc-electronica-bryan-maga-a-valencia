from abc import ABC, abstractmethod
from pathlib import Path

from semana2.eval1.miercoles.sensor_reading import SensorReading


class AlertStrategy(ABC):
    """Define cómo se debe enviar una alerta."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Envía una alerta."""
        raise NotImplementedError


class ConsoleAlertStrategy(AlertStrategy):
    """Manda la alerta directamente a la consola."""

    def send(self, message: str) -> None:
        print(f"ALERTA: {message}")


class FileAlertStrategy(AlertStrategy):
    """Guarda las alertas en un archivo de texto."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def send(self, message: str) -> None:
        # Agregamos cada alerta en una línea nueva para no borrar las anteriores.
        with self._file_path.open("a", encoding="utf-8") as file:
            file.write(f"ALERTA: {message}\n")


class AlertManager:
    """Se encarga de crear y enviar alertas usando una estrategia."""

    def __init__(self, strategy: AlertStrategy) -> None:
        self._strategy = strategy

    def send_alert(
        self,
        reading: SensorReading,
        reasons: list[str],
    ) -> None:
        # Convertimos las razones en un mensaje fácil de leer.
        reason_text = ", ".join(reasons)

        message = (
            f"Sensor {reading.sensor_id} detectó una anomalía: "
            f"{reason_text}. "
            f"Temperatura={reading.temperature}°C, "
            f"Humedad={reading.humidity}%"
        )

        self._strategy.send(message)