from datetime import datetime

from sqlalchemy.orm import Session

from app.models.reading import Reading
from app.schemas.reading import ReadingCreate


class ReadingRepository:
    """Repositorio encargado del acceso a la base
de datos de lecturas."""
    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
    ) -> list[Reading]:
        return (
            db.query(Reading)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        reading_id: int,
    ) -> Reading | None:
        return (
            db.query(Reading)
            .filter(Reading.id == reading_id)
            .first()
        )

    def create(
        self,
        db: Session,
        reading: ReadingCreate,
    ) -> Reading:
        db_reading = Reading(
            **reading.model_dump()
        )

        db.add(db_reading)
        db.commit()
        db.refresh(db_reading)

        return db_reading

    def delete(
        self,
        db: Session,
        db_reading: Reading,
    ) -> None:
        db.delete(db_reading)
        db.commit()

    def get_between_dates(
        self,
        db: Session,
        start: datetime,
        end: datetime,
    ) -> list[Reading]:
        return (
            db.query(Reading)
            .filter(
                Reading.timestamp >= start,
                Reading.timestamp <= end,
            )
            .all()
        )
