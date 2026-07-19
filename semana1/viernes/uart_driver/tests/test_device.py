from semana1.viernes.uart_driver.config import UartConfig
from semana1.viernes.uart_driver.device import UartDevice
from semana1.viernes.uart_driver.parsers import ModbusParser, NMEAParser


def test_device_works_with_modbus_parser() -> None:
    """Comprueba que el dispositivo pueda usar un parser Modbus."""
    config = UartConfig(
        port="COM3",
        baudrate=9600,
    )

    device = UartDevice(
        config=config,
        parser=ModbusParser(),
    )

    result = device.receive("PRESSURE:5.2")

    assert result["protocol"] == "Modbus"
    assert result["sensor"] == "PRESSURE"
    assert result["value"] == 5.2


def test_device_works_with_nmea_parser() -> None:
    """Comprueba que podamos cambiar el parser sin tocar el dispositivo."""
    config = UartConfig(
        port="COM3",
        baudrate=4800,
    )

    device = UartDevice(
        config=config,
        parser=NMEAParser(),
    )

    result = device.receive("$PRESSURE,7.5")

    assert result["protocol"] == "NMEA"
    assert result["sensor"] == "PRESSURE"
    assert result["value"] == 7.5


def test_device_returns_connection_info() -> None:
    """Comprueba que el dispositivo muestre su configuración."""
    config = UartConfig(
        port="COM3",
        baudrate=9600,
        timeout=2.0,
    )

    device = UartDevice(
        config=config,
        parser=ModbusParser(),
    )

    info = device.get_connection_info()

    assert info == "COM3 - 9600 baud - timeout 2.0s"