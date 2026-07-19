from dataclasses import dataclass


@dataclass(frozen=True)
class UartConfig:
    """Guarda la configuración de una conexión UART."""

    port: str
    baudrate: int
    timeout: float = 1.0

    def __post_init__(self) -> None:
        # Un baudrate menor o igual a cero no tiene sentido.
        if self.baudrate <= 0:
            raise ValueError("El baudrate debe ser mayor que cero.")

        # El puerto tampoco puede venir vacío.
        if not self.port.strip():
            raise ValueError("El puerto no puede estar vacío.")

        # El timeout no puede ser negativo.
        if self.timeout < 0:
            raise ValueError("El timeout no puede ser negativo.")