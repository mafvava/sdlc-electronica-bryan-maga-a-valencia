from fastapi import FastAPI

from app.database import Base, engine
from app.routers.readings import (
    router as reading_router,
)
from app.routers.sensors import (
    router as sensor_router,
)

app = FastAPI(
    title="SensorHub (EDSIA)",
    description="""
API REST para la gestión de sensores y lecturas.

## Funcionalidades

- Gestión de sensores.
- Registro de lecturas.
- Validaciones físicas.
- Paginación.
- Filtro por rango de fechas.
    """,
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(sensor_router)
app.include_router(reading_router)


@app.get("/")
def root() -> dict[str, str]:
    """Verifica que la API esté funcionando."""
    return {
        "message": "Bienvenido a SensorHub API",
    }
