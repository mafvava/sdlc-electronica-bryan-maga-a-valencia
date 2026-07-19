from abc import ABC, abstractmethod
from typing import Any


class MessageParser(ABC):
    """Contrato base para cualquier parser de mensajes UART."""

    @abstractmethod
    def parse(self, message: str) -> dict[str, Any]:
        """Convierte un mensaje recibido en datos que podamos usar."""
        ...


class ModbusParser(MessageParser):
    """Parser sencillo para mensajes de sensores usando Modbus."""

    def parse(self, message: str) -> dict[str, Any]:
        # Esperamos algo sencillo como: PRESSURE:5.2
        parts = message.split(":")

        if len(parts) != 2:
            raise ValueError("El mensaje Modbus no tiene un formato válido.")

        sensor = parts[0].strip()
        value = float(parts[1].strip())

        return {
            "protocol": "Modbus",
            "sensor": sensor,
            "value": value,
        }


class NMEAParser(MessageParser):
    """Parser sencillo para mensajes con formato NMEA."""

    def parse(self, message: str) -> dict[str, Any]:
        # Un ejemplo sencillo sería: $PRESSURE,5.2
        parts = message.split(",")

        if len(parts) != 2:
            raise ValueError("El mensaje NMEA no tiene un formato válido.")

        sensor = parts[0].replace("$", "").strip()
        value = float(parts[1].strip())

        return {
            "protocol": "NMEA",
            "sensor": sensor,
            "value": value,
        }