from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate


class SensorService:
    """Contiene la lógica de negocio relacionada con los sensores."""

    def __init__(self, db: Session):
        self.repository = SensorRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, sensor_id: int):
        sensor = self.repository.get_by_id(sensor_id)

        if sensor is None:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )

        return sensor

    def create(self, sensor: SensorCreate):
        return self.repository.create(sensor)

    def update(
        self,
        sensor_id: int,
        sensor: SensorCreate,
    ):
        updated = self.repository.update(sensor_id, sensor)

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )

        return updated

    def delete(self, sensor_id: int):
        deleted = self.repository.delete(sensor_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Sensor no encontrado.",
            )