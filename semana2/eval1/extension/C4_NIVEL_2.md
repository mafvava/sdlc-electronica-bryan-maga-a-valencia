# Diagrama C4 Nivel 2 - Sistema de monitoreo IoT

## Contexto

El sistema monitorea una bodega industrial donde tenemos 10 sensores de temperatura y humedad.

Cada sensor genera una lectura cada 30 segundos.

El sistema revisa las lecturas y detecta anomalías cuando:

- La temperatura es mayor a 35 °C.
- La humedad es mayor a 80%.

Cuando se encuentra una anomalía, se genera una alerta.

## Diagrama

```mermaid
C4Container

title Sistema de monitoreo IoT - C4 Nivel 2

Person(operator, "Operador", "Persona que revisa las alertas del sistema")

System_Boundary(iot_system, "Sistema de monitoreo IoT") {

    Container(sensors, "Sensores IoT", "Sensores de temperatura y humedad", "Generan una lectura cada 30 segundos")

    Container(simulator, "SensorSimulator", "Python", "Simula 10 sensores para pruebas e integración")

    Container(reading, "SensorReading", "Python", "Representa una lectura válida de temperatura y humedad")

    Container(detector, "AnomalyDetector", "Python", "Revisa las lecturas usando umbrales configurables")

    Container(alert_manager, "AlertManager", "Python", "Gestiona el envío de alertas usando una estrategia")

    Container(console_strategy, "ConsoleAlertStrategy", "Python", "Muestra las alertas en consola")

    Container(file_strategy, "FileAlertStrategy", "Python", "Guarda las alertas en un archivo")
}

Rel(sensors, reading, "Envía lecturas")
Rel(simulator, reading, "Genera lecturas simuladas")
Rel(reading, detector, "Envía lecturas")
Rel(detector, alert_manager, "Notifica anomalías")
Rel(alert_manager, console_strategy, "Envía alerta")
Rel(alert_manager, file_strategy, "Guarda alerta")
Rel(console_strategy, operator, "Muestra alertas")
Rel(file_strategy, operator, "Permite revisar alertas")