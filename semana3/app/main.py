from fastapi import FastAPI

from app.routers.readings import router as reading_router
from app.routers.sensors import router as sensor_router

app = FastAPI(
    title="SensorHub API",
    description="API para administrar sensores y sus lecturas.",
    version="1.0.0",
)

app.include_router(sensor_router)
app.include_router(reading_router)


@app.get("/")
def root() -> dict[str, str]:
    """Verifica que la API esté funcionando."""
    return {
        "message": "Bienvenido a SensorHub API",
    }