from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.sensor import (
    SensorCreate,
    SensorResponse,
)
from app.services.sensor_service import (
    SensorService,
)

router = APIRouter(
    prefix="/sensors",
    tags=["Sensores"],
)


@router.get(
    "/",
    response_model=list[SensorResponse],
)
def get_sensors(
    db: Session = Depends(get_db),
):
    service = SensorService(db)
    return service.get_all()


@router.get(
    "/{sensor_id}",
    response_model=SensorResponse,
)
def get_sensor(
    sensor_id: int,
    db: Session = Depends(get_db),
):
    service = SensorService(db)
    return service.get_by_id(sensor_id)


@router.post(
    "/",
    response_model=SensorResponse,
    status_code=201,
)
def create_sensor(
    sensor: SensorCreate,
    db: Session = Depends(get_db),
):
    service = SensorService(db)
    return service.create(sensor)


@router.put(
    "/{sensor_id}",
    response_model=SensorResponse,
)
def update_sensor(
    sensor_id: int,
    sensor: SensorCreate,
    db: Session = Depends(get_db),
):
    service = SensorService(db)
    return service.update(sensor_id, sensor)


@router.delete(
    "/{sensor_id}",
    status_code=204,
)
def delete_sensor(
    sensor_id: int,
    db: Session = Depends(get_db),
):
    service = SensorService(db)
    service.delete(sensor_id)
    return Response(status_code=204)
