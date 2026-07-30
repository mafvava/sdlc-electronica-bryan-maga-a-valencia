from datetime import datetime

from pydantic import BaseModel
from pydantic import field_validator


class ReadingCreate(BaseModel):
    sensor_id: int
    value: float

    timestamp: datetime | None = None


class ReadingResponse(BaseModel):
    id: int
    sensor_id: int
    value: float
    timestamp: datetime

    model_config = {
        "from_attributes": True,
    }