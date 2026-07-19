from typing import Any

from semana1.viernes.uart_driver.config import UartConfig
from semana1.viernes.uart_driver.parsers import MessageParser


class UartDevice:
    """Representa un dispositivo UART que recibe mensajes de sensores."""

    def __init__(
        self,
        config: UartConfig,
        parser: MessageParser,
    ) -> None:
        # El dispositivo recibe lo que necesita desde afuera.
        # Así no queda amarrado a un parser específico.
        self.config = config
        self.parser = parser

    def receive(self, message: str) -> dict[str, Any]:
        """Recibe un mensaje y lo procesa usando el parser configurado."""
        return self.parser.parse(message)

    def get_connection_info(self) -> str:
        """Devuelve los datos básicos de conexión del dispositivo."""
        return (
            f"{self.config.port} - "
            f"{self.config.baudrate} baud - "
            f"timeout {self.config.timeout}s"
        )