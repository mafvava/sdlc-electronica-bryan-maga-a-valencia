from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate


class ReadingService:
    """Lógica de negocio para las lecturas."""

    def __init__(self, db: Session):
        self.reading_repository = ReadingRepository(db)
        self.sensor_repository = SensorRepository(db)

    def create(self, reading: ReadingCreate):
        sensor = self.sensor_repository.get_by_id(
            reading.sensor_id
        )

        if sensor is None:
            raise HTTPException(
                status_code=404,
                detail="El sensor no existe.",
            )

        # Validación física

        if sensor.sensor_type == "temperature":

            if reading.value < -50 or reading.value > 100:
                raise HTTPException(
                    status_code=422,
                    detail="Temperatura fuera de rango.",
                )

        elif sensor.sensor_type == "humidity":

            if reading.value < 0 or reading.value > 100:
                raise HTTPException(
                    status_code=422,
                    detail="Humedad fuera de rango.",
                )

        return self.reading_repository.create(reading)

    def get_all(
        self,
        skip: int,
        limit: int,
    ):
        return self.reading_repository.get_all(
            skip,
            limit,
        )

    def get_by_id(
        self,
        reading_id: int,
    ):
        reading = self.reading_repository.get_by_id(
            reading_id
        )

        if reading is None:
            raise HTTPException(
                status_code=404,
                detail="Lectura no encontrada.",
            )

        return reading

    def delete(
        self,
        reading_id: int,
    ):
        deleted = self.reading_repository.delete(
            reading_id
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Lectura no encontrada.",
            )

    def get_between_dates(
        self,
        start: datetime,
        end: datetime,
    ):
        return self.reading_repository.get_between_dates(
            start,
            end,
        )