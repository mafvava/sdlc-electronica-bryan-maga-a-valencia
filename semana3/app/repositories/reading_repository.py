from datetime import datetime

from sqlalchemy.orm import Session

from app.models.reading import Reading
from app.schemas.reading import ReadingCreate


class ReadingRepository:
    """Operaciones de base de datos para las lecturas."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, reading: ReadingCreate) -> Reading:
        db_reading = Reading(**reading.model_dump())

        self.db.add(db_reading)
        self.db.commit()
        self.db.refresh(db_reading)

        return db_reading

    def get_by_id(self, reading_id: int) -> Reading | None:
        return (
            self.db.query(Reading)
            .filter(Reading.id == reading_id)
            .first()
        )

    def get_all(
        self,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Reading]:
        return (
            self.db.query(Reading)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_between_dates(
        self,
        start: datetime,
        end: datetime,
    ) -> list[Reading]:
        return (
            self.db.query(Reading)
            .filter(
                Reading.timestamp >= start,
                Reading.timestamp <= end,
            )
            .all()
        )

    def delete(self, reading_id: int) -> bool:
        reading = self.get_by_id(reading_id)

        if reading is None:
            return False

        self.db.delete(reading)
        self.db.commit()

        return True