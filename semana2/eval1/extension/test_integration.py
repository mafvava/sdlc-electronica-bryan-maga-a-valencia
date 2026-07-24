from pathlib import Path

from semana2.eval1.extension.sensor_simulator import SensorSimulator
from semana2.eval1.jueves.anomaly_detector import (
    AnomalyDetector,
    AnomalyThresholds,
)
from semana2.eval1.viernes.alert_manager import (
    AlertManager,
    FileAlertStrategy,
)


def test_ten_sensors_run_sixty_cycles_and_generate_alerts(
    tmp_path: Path,
) -> None:
    """Comprueba el flujo completo de 10 sensores durante 60 ciclos."""
    simulator = SensorSimulator(
        sensor_count=10,
        seed=123,
        temperature_mean=30.0,
        temperature_stddev=6.0,
        humidity_mean=65.0,
        humidity_stddev=15.0,
    )

    # Definimos los límites que vamos a usar para detectar anomalías.
    thresholds = AnomalyThresholds(
        max_temperature=35.0,
        max_humidity=80.0,
    )

    detector = AnomalyDetector(thresholds)

    # Usamos un archivo temporal para guardar las alertas.
    alert_file = tmp_path / "alerts.log"
    alert_strategy = FileAlertStrategy(alert_file)
    alert_manager = AlertManager(alert_strategy)

    # Generamos 60 ciclos con los 10 sensores.
    cycles = simulator.generate_cycles(cycles=60)

    total_readings = 0
    total_anomalies = 0

    for cycle in cycles:
        for reading in cycle:
            total_readings += 1

            # Revisamos si la lectura supera alguno de los límites.
            if detector.is_anomalous(reading):
                total_anomalies += 1

                # Obtenemos las razones de la anomalía.
                reasons = detector.reasons(reading)

                # El AlertManager recibe la lectura completa y las razones.
                alert_manager.send_alert(
                    reading,
                    reasons,
                )

    # Son 10 sensores multiplicados por los 60 ciclos.
    assert total_readings == 600

    # Con estos valores esperamos encontrar algunas anomalías.
    assert total_anomalies > 0

    # Comprobamos que se haya guardado una alerta por cada anomalía.
    saved_alerts = alert_file.read_text(
        encoding="utf-8",
    ).splitlines()

    assert len(saved_alerts) == total_anomalies