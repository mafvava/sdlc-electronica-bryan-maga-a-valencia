from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    sensor_type: Mapped[str] = mapped_column(String(30))
    unit: Mapped[str] = mapped_column(String(10))