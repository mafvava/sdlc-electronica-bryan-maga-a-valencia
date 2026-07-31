from sqlalchemy.orm import Session

from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate


class SensorRepository:
    """Repositorio encargado del acceso a la base de datos de sensores."""

    def get_all(self, db: Session) -> list[Sensor]:
        return db.query(Sensor).all()

    def get_by_id(
        self,
        db: Session,
        sensor_id: int,
    ) -> Sensor | None:
        return (
            db.query(Sensor)
            .filter(Sensor.id == sensor_id)
            .first()
        )

    def get_by_name(
        self,
        db: Session,
        name: str,
    ) -> Sensor | None:
        return (
            db.query(Sensor)
            .filter(Sensor.name == name)
            .first()
        )

    def create(
        self,
        db: Session,
        sensor: SensorCreate,
    ) -> Sensor:
        db_sensor = Sensor(
            name=sensor.name,
            sensor_type=sensor.sensor_type,
            unit=sensor.unit,
            location=sensor.location,
        )

        db.add(db_sensor)
        db.commit()
        db.refresh(db_sensor)

        return db_sensor

    def update(
        self,
        db: Session,
        db_sensor: Sensor,
        sensor: SensorCreate,
    ) -> Sensor:
        db_sensor.name = sensor.name
        db_sensor.sensor_type = sensor.sensor_type
        db_sensor.unit = sensor.unit
        db_sensor.location = sensor.location

        db.commit()
        db.refresh(db_sensor)

        return db_sensor

    def delete(
        self,
        db: Session,
        db_sensor: Sensor,
    ) -> None:
        db.delete(db_sensor)
        db.commit()