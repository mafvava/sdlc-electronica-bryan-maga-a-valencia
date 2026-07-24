from datetime import datetime

from random import Random

from semana2.eval1.miercoles.sensor_reading import SensorReading


class SensorSimulator:
    """Simula lecturas de temperatura y humedad de varios sensores."""

    def __init__(
        self,
        sensor_count: int = 10,
        seed: int | None = None,
        temperature_mean: float = 25.0,
        temperature_stddev: float = 4.0,
        humidity_mean: float = 60.0,
        humidity_stddev: float = 10.0,
    ) -> None:
        if sensor_count <= 0:
            raise ValueError("La cantidad de sensores debe ser mayor que cero.")

        if temperature_stddev <= 0:
            raise ValueError(
                "La desviación de temperatura debe ser mayor que cero."
            )

        if humidity_stddev <= 0:
            raise ValueError(
                "La desviación de humedad debe ser mayor que cero."
            )

        self.sensor_count = sensor_count
        self.temperature_mean = temperature_mean
        self.temperature_stddev = temperature_stddev
        self.humidity_mean = humidity_mean
        self.humidity_stddev = humidity_stddev

        # La semilla nos sirve para repetir los mismos resultados en los tests.
        self._random = Random(seed)

    def generate_readings(self) -> list[SensorReading]:
        """Genera una lectura para cada sensor."""
        readings: list[SensorReading] = []

        # Usamos la misma hora para todas las lecturas de este ciclo.
        timestamp = datetime.now()

        for sensor_number in range(1, self.sensor_count + 1):
            temperature = self._random.gauss(
                self.temperature_mean,
                self.temperature_stddev,
            )

            humidity = self._random.gauss(
                self.humidity_mean,
                self.humidity_stddev,
            )

            # Limitamos la humedad para que siempre tenga un valor válido.
            humidity = max(0.0, min(100.0, humidity))

            readings.append(
                SensorReading(
                    sensor_id=f"SENSOR-{sensor_number:02d}",
                    temperature=temperature,
                    humidity=humidity,
                    timestamp=timestamp,
                )
            )

        return readings

    def generate_cycles(
        self,
        cycles: int = 60,
    ) -> list[list[SensorReading]]:
        """Genera varias rondas de lecturas de todos los sensores."""
        if cycles <= 0:
            raise ValueError(
                "La cantidad de ciclos debe ser mayor que cero."
            )

        return [
            self.generate_readings()
            for _ in range(cycles)
        ]