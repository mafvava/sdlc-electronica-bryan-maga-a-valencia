from semana1.martes.fsm_demo import TrafficLight, TrafficLightState


def test_initial_state_is_red() -> None:
    """Verifica que el semáforo inicie en rojo."""
    traffic_light = TrafficLight()

    assert traffic_light.state is TrafficLightState.RED


def test_red_transitions_to_green() -> None:
    """Verifica la transición de RED a GREEN."""
    traffic_light = TrafficLight()

    traffic_light.transition()

    assert traffic_light.state is TrafficLightState.GREEN


def test_complete_cycle_returns_to_red() -> None:
    """Verifica que un ciclo completo termine nuevamente en RED."""
    traffic_light = TrafficLight()

    traffic_light.transition()  # RED → GREEN
    traffic_light.transition()  # GREEN → YELLOW
    traffic_light.transition()  # YELLOW → RED

    assert traffic_light.state is TrafficLightState.RED


def test_cycle_count_increments_after_complete_cycle() -> None:
    """Verifica que el contador aumente después de un ciclo completo."""
    traffic_light = TrafficLight()

    assert traffic_light.cycle_count == 0

    traffic_light.transition()  # RED → GREEN
    traffic_light.transition()  # GREEN → YELLOW
    traffic_light.transition()  # YELLOW → RED

    assert traffic_light.cycle_count == 1