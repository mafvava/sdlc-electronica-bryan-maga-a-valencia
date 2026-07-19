from semana1.miercoles.solid_srp_ocp_lsp import (
    BadOfflineSensor,
    BadPressureSensor,
    HighPressureRule,
    IndustrialPressureSensor,
    LowPressureRule,
    PressureAlarm,
    PressureRepository,
    PressureSensor,
    PressureValidator,
    SimulatedPressureSensor,
    process_pressure_sensor,
)


# ============================================================
# SRP - Single Responsibility Principle
# ============================================================


def test_srp_good_classes_have_separate_responsibilities() -> None:
    """Verifica que las clases correctas de SRP trabajen por separado."""
    sensor = PressureSensor()
    validator = PressureValidator()
    repository = PressureRepository()

    pressure = sensor.read()

    assert pressure == 2.5
    assert validator.is_valid(pressure) is True

    repository.save(pressure)


def test_srp_bad_class_combines_multiple_responsibilities() -> None:
    """Verifica el comportamiento del ejemplo que viola SRP."""
    sensor = BadPressureSensor()

    pressure = sensor.read()

    assert pressure == 2.5
    assert sensor.validate(pressure) is True


# ============================================================
# OCP - Open/Closed Principle
# ============================================================


def test_ocp_high_pressure_rule() -> None:
    """Verifica una regla de alarma de presión alta."""
    alarm = PressureAlarm(HighPressureRule(limit=10))

    assert alarm.check(12) is True
    assert alarm.check(8) is False


def test_ocp_low_pressure_rule() -> None:
    """Verifica una regla de alarma de presión baja."""
    alarm = PressureAlarm(LowPressureRule(limit=1))

    assert alarm.check(0.5) is True
    assert alarm.check(2) is False


# ============================================================
# LSP - Liskov Substitution Principle
# ============================================================


def test_lsp_valid_sensors_are_interchangeable() -> None:
    """Verifica que los sensores válidos puedan sustituirse."""
    industrial_sensor = IndustrialPressureSensor()
    simulated_sensor = SimulatedPressureSensor()

    industrial_reading = process_pressure_sensor(industrial_sensor)
    simulated_reading = process_pressure_sensor(simulated_sensor)

    assert industrial_reading.value == 2.5
    assert industrial_reading.unit == "bar"

    assert simulated_reading.value == 2.5
    assert simulated_reading.unit == "bar"


def test_lsp_bad_subclass_breaks_expected_contract() -> None:
    """Verifica el comportamiento de una implementación que viola LSP."""
    sensor = BadOfflineSensor()

    try:
        sensor.read()
    except RuntimeError as error:
        assert str(error) == "Sensor fuera de línea"
    else:
        raise AssertionError("Se esperaba un RuntimeError")