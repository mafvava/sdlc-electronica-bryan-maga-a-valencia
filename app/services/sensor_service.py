from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate


class SensorService:
    """Contiene la lógica de negocio relacionada con los sensores."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = SensorRepository()

    def get_all(self):
        return self.repository.get_all(self.db)

    def get_by_id(self, sensor_id: int):
        sensor = self.repository.get_by_id(
            self.db,
            sensor_id,
        )

        if sensor is None:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )

        return sensor

    def create(
        self,
        sensor: SensorCreate,
    ):
        existing_sensor = self.repository.get_by_name(
            self.db,
            sensor.name,
        )

        if existing_sensor is not None:
            raise HTTPException(
                status_code=409,
                detail="Ya existe un sensor con ese nombre.",
            )

        return self.repository.create(
            self.db,
            sensor,
        )

    def update(
        self,
        sensor_id: int,
        sensor: SensorCreate,
    ):
        db_sensor = self.repository.get_by_id(
            self.db,
            sensor_id,
        )

        if db_sensor is None:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )

        return self.repository.update(
            self.db,
            db_sensor,
            sensor,
        )

    def delete(self, sensor_id: int):
        db_sensor = self.repository.get_by_id(
            self.db,
            sensor_id,
        )

        if db_sensor is None:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )

        self.repository.delete(
            self.db,
            db_sensor,
        )