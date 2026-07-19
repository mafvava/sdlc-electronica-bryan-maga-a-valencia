from typing import Protocol


# ============================================================
# ISP - Interface Segregation Principle
# ============================================================


# ❌ EJEMPLO "MAL"
# Aquí tenemos una interfaz gigante que obliga a un sensor
# a implementar cosas que realmente no necesita.
class BadIndustrialSensor:
    """Ejemplo que rompe el principio ISP."""

    def read_pressure(self) -> float:
        """Lee la presión del sensor."""
        return 2.5

    def read_temperature(self) -> float:
        """Lee la temperatura del sensor."""
        return 25.0

    def calibrate(self) -> None:
        """Calibra el sensor."""
        print("Sensor calibrado")

    def send_data(self) -> None:
        """Envía los datos del sensor."""
        print("Datos enviados")


# ❌ Este sensor solo mide presión, pero la interfaz anterior
# lo obliga a tener métodos que no necesita.
class BadPressureSensor:
    """Sensor de presión con una interfaz demasiado grande."""

    def read_pressure(self) -> float:
        """Lee la presión."""
        return 2.5

    def read_temperature(self) -> float:
        """Este método no tiene sentido para este sensor."""
        raise NotImplementedError

    def calibrate(self) -> None:
        """Calibra el sensor."""
        print("Sensor calibrado")

    def send_data(self) -> None:
        """Envía los datos."""
        print("Datos enviados")


# ✅ EJEMPLO "BIEN"
# En lugar de tener una interfaz gigante, la dividimos
# en interfaces pequeñas y específicas.
class PressureReader(Protocol):
    """Define lo mínimo necesario para leer presión."""

    def read_pressure(self) -> float:
        """Obtiene una lectura de presión."""
        ...


class Calibratable(Protocol):
    """Define el comportamiento de un dispositivo calibrable."""

    def calibrate(self) -> None:
        """Calibra el dispositivo."""
        ...


class DataSender(Protocol):
    """Define el comportamiento para enviar datos."""

    def send_data(self) -> None:
        """Envía los datos."""
        ...


class IndustrialPressureSensor:
    """Sensor que solo necesita leer presión."""

    def read_pressure(self) -> float:
        """Devuelve una lectura de presión."""
        return 2.5


class AdvancedPressureSensor:
    """Sensor de presión que además puede calibrarse y enviar datos."""

    def read_pressure(self) -> float:
        """Devuelve una lectura de presión."""
        return 2.5

    def calibrate(self) -> None:
        """Calibra el sensor."""
        print("Sensor calibrado")

    def send_data(self) -> None:
        """Envía los datos."""
        print("Datos enviados")


def get_pressure(sensor: PressureReader) -> float:
    """Obtiene presión sin exigir funciones que no necesita."""
    return sensor.read_pressure()


# ============================================================
# DIP - Dependency Inversion Principle
# ============================================================


# ❌ EJEMPLO "MAL"
# Esta clase depende directamente de una implementación concreta.
class BadPressureFileLogger:
    """Guarda las lecturas directamente en un archivo."""

    def save(self, pressure: float) -> None:
        """Guarda una lectura en un archivo."""
        print(f"Guardando {pressure} bar en archivo")


class BadPressureProcessor:
    """Procesador acoplado directamente al logger de archivos."""

    def __init__(self) -> None:
        self.logger = BadPressureFileLogger()

    def process(self, pressure: float) -> None:
        """Procesa y guarda una lectura."""
        self.logger.save(pressure)


# ✅ EJEMPLO "BIEN"
# Creamos una abstracción para que el procesador
# no dependa de una implementación concreta.
class PressureStorage(Protocol):
    """Define cómo guardar una lectura de presión."""

    def save(self, pressure: float) -> None:
        """Guarda una lectura."""
        ...


class FilePressureStorage:
    """Guarda las lecturas en un archivo."""

    def save(self, pressure: float) -> None:
        """Simula guardar una lectura en un archivo."""
        print(f"Guardando {pressure} bar en archivo")


class MemoryPressureStorage:
    """Guarda las lecturas temporalmente en memoria."""

    def __init__(self) -> None:
        self.values: list[float] = []

    def save(self, pressure: float) -> None:
        """Guarda una lectura en la lista."""
        self.values.append(pressure)


class PressureProcessor:
    """Procesa lecturas sin depender de una implementación concreta."""

    def __init__(self, storage: PressureStorage) -> None:
        self.storage = storage

    def process(self, pressure: float) -> None:
        """Procesa una lectura y la manda al almacenamiento."""
        self.storage.save(pressure)