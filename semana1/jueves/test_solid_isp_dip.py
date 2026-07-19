from semana1.jueves.solid_isp_dip import (
    AdvancedPressureSensor,
    BadPressureProcessor,
    BadPressureSensor,
    FilePressureStorage,
    IndustrialPressureSensor,
    MemoryPressureStorage,
    PressureProcessor,
    get_pressure,
)


# ============================================================
# ISP - Interface Segregation Principle
# ============================================================


def test_isp_sensor_can_use_only_the_interface_it_needs() -> None:
    """Verifica que un sensor pueda trabajar solo con lectura de presión."""
    sensor = IndustrialPressureSensor()

    pressure = get_pressure(sensor)

    assert pressure == 2.5


def test_isp_advanced_sensor_can_use_multiple_capabilities() -> None:
    """Verifica que un sensor avanzado pueda usar varias funciones."""
    sensor = AdvancedPressureSensor()

    assert sensor.read_pressure() == 2.5

    sensor.calibrate()
    sensor.send_data()


# ============================================================
# DIP - Dependency Inversion Principle
# ============================================================


def test_dip_processor_works_with_memory_storage() -> None:
    """Verifica la inyección de un almacenamiento en memoria."""
    storage = MemoryPressureStorage()
    processor = PressureProcessor(storage)

    processor.process(2.5)
    processor.process(3.0)

    assert storage.values == [2.5, 3.0]


def test_dip_processor_works_with_file_storage() -> None:
    """Verifica que el procesador pueda usar otro almacenamiento."""
    storage = FilePressureStorage()
    processor = PressureProcessor(storage)

    processor.process(2.5)

    assert isinstance(processor.storage, FilePressureStorage)


# ============================================================
# EJEMPLOS "MAL"
# ============================================================


def test_isp_bad_sensor_shows_the_problem() -> None:
    """Muestra que el sensor malo necesita métodos que no usa."""
    sensor = BadPressureSensor()

    assert sensor.read_pressure() == 2.5


def test_dip_bad_example_is_tightly_coupled() -> None:
    """Muestra que el ejemplo malo está acoplado al almacenamiento."""
    processor = BadPressureProcessor()

    assert isinstance(processor.logger, object)