from datetime import datetime, timezone
from pathlib import Path

from semana2.eval1.miercoles.sensor_reading import SensorReading
from semana2.eval1.viernes.alert_manager import (
    AlertManager,
    ConsoleAlertStrategy,
    FileAlertStrategy,
)


def create_reading() -> SensorReading:
    return SensorReading(
        sensor_id="sensor-01",
        temperature=40.0,
        humidity=85.0,
        timestamp=datetime.now(timezone.utc),
    )


def test_console_alert_strategy_sends_alert(capsys) -> None:
    manager = AlertManager(ConsoleAlertStrategy())

    manager.send_alert(
        create_reading(),
        ["temperature", "humidity"],
    )

    captured = capsys.readouterr()

    assert "ALERTA:" in captured.out
    assert "sensor-01" in captured.out
    assert "temperature" in captured.out
    assert "humidity" in captured.out


def test_file_alert_strategy_saves_alert(tmp_path: Path) -> None:
    file_path = tmp_path / "alerts.log"

    manager = AlertManager(FileAlertStrategy(file_path))

    manager.send_alert(
        create_reading(),
        ["temperature"],
    )

    content = file_path.read_text(encoding="utf-8")

    assert "ALERTA:" in content
    assert "sensor-01" in content
    assert "temperature" in content


def test_file_alert_strategy_keeps_multiple_alerts(tmp_path: Path) -> None:
    file_path = tmp_path / "alerts.log"

    manager = AlertManager(FileAlertStrategy(file_path))

    manager.send_alert(
        create_reading(),
        ["temperature"],
    )

    manager.send_alert(
        create_reading(),
        ["humidity"],
    )

    lines = file_path.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 2
    assert "temperature" in lines[0]
    assert "humidity" in lines[1]


def test_alert_manager_uses_injected_strategy(tmp_path: Path) -> None:
    file_path = tmp_path / "alerts.log"
    strategy = FileAlertStrategy(file_path)

    manager = AlertManager(strategy)

    manager.send_alert(
        create_reading(),
        ["temperature"],
    )

    assert file_path.exists()