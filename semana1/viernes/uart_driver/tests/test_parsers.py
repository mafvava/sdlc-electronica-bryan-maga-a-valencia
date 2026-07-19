import pytest

from semana1.viernes.uart_driver.parsers import ModbusParser, NMEAParser


def test_modbus_parser_reads_pressure_message() -> None:
    """Comprueba que Modbus lea bien una presión."""
    parser = ModbusParser()

    result = parser.parse("PRESSURE:5.2")

    assert result["protocol"] == "Modbus"
    assert result["sensor"] == "PRESSURE"
    assert result["value"] == 5.2


def test_modbus_parser_rejects_invalid_message() -> None:
    """Comprueba que Modbus rechace un mensaje mal formado."""
    parser = ModbusParser()

    with pytest.raises(ValueError, match="formato válido"):
        parser.parse("PRESSURE-5.2")


def test_nmea_parser_reads_pressure_message() -> None:
    """Comprueba que NMEA lea bien una presión."""
    parser = NMEAParser()

    result = parser.parse("$PRESSURE,5.2")

    assert result["protocol"] == "NMEA"
    assert result["sensor"] == "PRESSURE"
    assert result["value"] == 5.2


def test_nmea_parser_rejects_invalid_message() -> None:
    """Comprueba que NMEA rechace un mensaje mal formado."""
    parser = NMEAParser()

    with pytest.raises(ValueError, match="formato válido"):
        parser.parse("$PRESSURE;5.2")


def test_modbus_parser_converts_value_to_float() -> None:
    """Comprueba que el valor recibido termine siendo un float."""
    parser = ModbusParser()

    result = parser.parse("PRESSURE:10")

    assert isinstance(result["value"], float)


def test_nmea_parser_converts_value_to_float() -> None:
    """Comprueba que NMEA convierta el valor recibido a float."""
    parser = NMEAParser()

    result = parser.parse("$PRESSURE,10")

    assert isinstance(result["value"], float)