from pathlib import Path

from semana1.viernes.uart_driver.recorder import JsonLinesRecorder


def test_recorder_saves_one_reading(tmp_path: Path) -> None:
    """Comprueba que podamos guardar una lectura."""
    file_path = tmp_path / "readings.jsonl"
    recorder = JsonLinesRecorder(file_path)

    reading = {
        "sensor": "PRESSURE",
        "value": 5.2,
        "unit": "bar",
    }

    recorder.record(reading)

    records = recorder.read_all()

    assert records == [reading]


def test_recorder_saves_multiple_readings(tmp_path: Path) -> None:
    """Comprueba que podamos guardar varias lecturas."""
    file_path = tmp_path / "readings.jsonl"
    recorder = JsonLinesRecorder(file_path)

    first_reading = {
        "sensor": "PRESSURE",
        "value": 5.2,
    }

    second_reading = {
        "sensor": "PRESSURE",
        "value": 6.1,
    }

    recorder.record(first_reading)
    recorder.record(second_reading)

    records = recorder.read_all()

    assert records == [first_reading, second_reading]


def test_recorder_returns_empty_list_when_file_does_not_exist(
    tmp_path: Path,
) -> None:
    """Comprueba que un archivo que todavía no existe no cause problemas."""
    file_path = tmp_path / "readings.jsonl"
    recorder = JsonLinesRecorder(file_path)

    assert recorder.read_all() == []