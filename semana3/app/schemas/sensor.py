from pydantic import BaseModel, Field, field_validator


VALID_SENSOR_TYPES = {"temperature", "humidity"}

VALID_UNITS = {
    "temperature": "C",
    "humidity": "%",
}


class SensorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    sensor_type: str
    unit: str

    @field_validator("sensor_type")
    @classmethod
    def validate_sensor_type(cls, value: str) -> str:
        if value not in VALID_SENSOR_TYPES:
            raise ValueError("Tipo de sensor no válido.")
        return value

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str, info) -> str:
        sensor_type = info.data.get("sensor_type")

        if sensor_type and VALID_UNITS[sensor_type] != value:
            raise ValueError("Unidad incorrecta para el tipo de sensor.")

        return value


class SensorResponse(SensorCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }