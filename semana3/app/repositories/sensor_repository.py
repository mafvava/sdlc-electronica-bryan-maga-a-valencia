from sqlalchemy.orm import Session

from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate


class SensorRepository:
    """Se encarga de todas las operaciones de base de datos para Sensor."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Sensor]:
        return self.db.query(Sensor).all()

    def get_by_id(self, sensor_id: int) -> Sensor | None:
        return (
            self.db.query(Sensor)
            .filter(Sensor.id == sensor_id)
            .first()
        )

    def create(self, sensor: SensorCreate) -> Sensor:
        db_sensor = Sensor(**sensor.model_dump())

        self.db.add(db_sensor)
        self.db.commit()
        self.db.refresh(db_sensor)

        return db_sensor

    def update(self, sensor_id: int, sensor: SensorCreate) -> Sensor | None:
        db_sensor = self.get_by_id(sensor_id)

        if db_sensor is None:
            return None

        for key, value in sensor.model_dump().items():
            setattr(db_sensor, key, value)

        self.db.commit()
        self.db.refresh(db_sensor)

        return db_sensor

    def delete(self, sensor_id: int) -> bool:
        db_sensor = self.get_by_id(sensor_id)

        if db_sensor is None:
            return False

        self.db.delete(db_sensor)
        self.db.commit()

        return True