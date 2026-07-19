import pytest

from semana1.viernes.uart_driver.config import UartConfig

def test_uart_config_is_created_correctly() -> None:
    """Verifica que la configuración se cree con los datos correctos."""
    config = UartConfig(
        port="COM3",
        baudrate=9600,
        timeout=1.0,
    )

    assert config.port == "COM3"
    assert config.baudrate == 9600
    assert config.timeout == 1.0


def test_uart_config_rejects_invalid_baudrate() -> None:
    """Verifica que no aceptemos un baudrate inválido."""
    with pytest.raises(ValueError, match="baudrate"):
        UartConfig(
            port="COM3",
            baudrate=0,
        )


def test_uart_config_is_immutable() -> None:
    """Verifica que no podamos cambiar la configuración después de crearla."""
    config = UartConfig(
        port="COM3",
        baudrate=9600,
    )

    with pytest.raises(AttributeError):
        config.baudrate = 115200  # type: ignore[misc]