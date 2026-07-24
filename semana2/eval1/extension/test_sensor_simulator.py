import pytest

from semana2.eval1.extension.sensor_simulator import SensorSimulator


def test_simulator_generates_ten_sensor_readings() -> None:
    """Comprueba que se genere una lectura por cada uno de los 10 sensores."""
    simulator = SensorSimulator(sensor_count=10, seed=123)

    readings = simulator.generate_readings()

    assert len(readings) == 10
    assert [reading.sensor_id for reading in readings] == [
        "SENSOR-01",
        "SENSOR-02",
        "SENSOR-03",
        "SENSOR-04",
        "SENSOR-05",
        "SENSOR-06",
        "SENSOR-07",
        "SENSOR-08",
        "SENSOR-09",
        "SENSOR-10",
    ]


def test_simulator_generates_sixty_cycles() -> None:
    """Comprueba que podamos generar los 60 ciclos pedidos."""
    simulator = SensorSimulator(sensor_count=10, seed=123)

    cycles = simulator.generate_cycles(cycles=60)

    assert len(cycles) == 60
    assert all(len(cycle) == 10 for cycle in cycles)


def test_simulator_uses_gaussian_distribution() -> None:
    """Comprueba que el simulador genere valores alrededor de la media configurada."""
    simulator = SensorSimulator(
        sensor_count=100,
        seed=123,
        temperature_mean=25.0,
        temperature_stddev=2.0,
    )

    readings = simulator.generate_readings()
    temperatures = [reading.temperature for reading in readings]

    average = sum(temperatures) / len(temperatures)

    assert 20.0 < average < 30.0


def test_simulator_rejects_invalid_sensor_count() -> None:
    """Comprueba que no aceptemos cero sensores."""
    with pytest.raises(ValueError):
        SensorSimulator(sensor_count=0)


def test_simulator_rejects_invalid_cycles() -> None:
    """Comprueba que no aceptemos cero ciclos."""
    simulator = SensorSimulator()

    with pytest.raises(ValueError):
        simulator.generate_cycles(cycles=0)