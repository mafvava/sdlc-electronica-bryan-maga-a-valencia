from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class SensorCreate(BaseModel):
    """Datos necesarios para crear un sensor."""

    name: str = Field(
        min_length=1, max_length=100
    )

    sensor_type: Literal[
        "temperature",
        "humidity",
        "pressure",
        "co2",
    ]

    unit: str

    location: str = Field(
        min_length=1, max_length=100
    )


class SensorResponse(BaseModel):
    """Representa un sensor almacenado."""

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    name: str
    sensor_type: str
    unit: str
    location: str
    created_at: datetime
