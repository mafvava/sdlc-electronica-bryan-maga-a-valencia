from enum import Enum, auto


class TrafficLightState(Enum):
    """Estados posibles del semáforo."""

    RED = auto()
    GREEN = auto()
    YELLOW = auto()


class TrafficLight:
    """Máquina de estados orientada a objetos para un semáforo."""

    def __init__(self) -> None:
        self._state = TrafficLightState.RED
        self._cycle_count = 0

    @property
    def state(self) -> TrafficLightState:
        """Devuelve el estado actual del semáforo."""
        return self._state

    @property
    def cycle_count(self) -> int:
        """Devuelve el número de ciclos completos realizados."""
        return self._cycle_count

    def transition(self) -> None:
        """Avanza el semáforo al siguiente estado."""
        if self._state is TrafficLightState.RED:
            self._state = TrafficLightState.GREEN

        elif self._state is TrafficLightState.GREEN:
            self._state = TrafficLightState.YELLOW

        elif self._state is TrafficLightState.YELLOW:
            self._state = TrafficLightState.RED
            self._cycle_count += 1