from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)

DATABASE_URL = "sqlite:///sensorhub.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """Clase base para todos los modelos ORM."""


def get_db():
    """Proporciona una sesión de base de datos
para cada petición."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
