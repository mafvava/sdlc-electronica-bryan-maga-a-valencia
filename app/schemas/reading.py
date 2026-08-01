from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReadingCreate(BaseModel):
    """Datos necesarios para crear una lectura."""

    sensor_id: int
    value: float
    timestamp: datetime


class ReadingResponse(BaseModel):
    """Representa una lectura almacenada."""

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    sensor_id: int
    value: float
    timestamp: datetime
