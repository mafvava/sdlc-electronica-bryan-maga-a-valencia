from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.reading_repository import (
    ReadingRepository,
)
from app.repositories.sensor_repository import (
    SensorRepository,
)
from app.schemas.reading import ReadingCreate


class ReadingService:
    """Contiene la lógica de negocio
    relacionada con las lecturas."""

    def __init__(self, db: Session):
        self.db = db
        self.reading_repository = (
            ReadingRepository()
        )
        self.sensor_repository = (
            SensorRepository()
        )

    def create(
        self,
        reading: ReadingCreate,
    ):
        sensor = self.sensor_repository.get_by_id(
            self.db,
            reading.sensor_id,
        )

        if sensor is None:
            raise HTTPException(
                status_code=404,
                detail="El sensor no existe.",
            )

        if sensor.sensor_type == "temperature":
            if (
                reading.value < -50
                or reading.value > 100
            ):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        "Temperatura fuera de "
                        "rango."
                    ),
                )

        elif sensor.sensor_type == "humidity":
            if (
                reading.value < 0
                or reading.value > 100
            ):
                raise HTTPException(
                    status_code=422,
                    detail=(
                        "Humedad fuera de "
                        "rango."
                    ),
                )

        return self.reading_repository.create(
            self.db,
            reading,
        )

    def get_all(
        self,
        skip: int,
        limit: int,
    ):
        return self.reading_repository.get_all(
            self.db,
            skip,
            limit,
        )

    def get_by_id(
        self,
        reading_id: int,
    ):
        reading = (
            self.reading_repository.get_by_id(
                self.db,
                reading_id,
            )
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
        db_reading = (
            self.reading_repository.get_by_id(
                self.db,
                reading_id,
            )
        )

        if db_reading is None:
            raise HTTPException(
                status_code=404,
                detail="Lectura no encontrada.",
            )

        self.reading_repository.delete(
            self.db,
            db_reading,
        )

    def get_between_dates(
        self,
        start: datetime,
        end: datetime,
    ):
        repository = self.reading_repository

        return repository.get_between_dates(
            self.db,
            start,
            end,
        )