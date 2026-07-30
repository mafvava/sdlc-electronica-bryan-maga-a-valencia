from fastapi import FastAPI

from app.database import Base
from app.database import engine
from app.routers.readings import router as reading_router
from app.routers.sensors import router as sensor_router


app = FastAPI(
    title="SensorHub API",
    description="API para la gestión de sensores y lecturas.",
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