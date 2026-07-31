from datetime import datetime

from fastapi import APIRouter, Depends, Query, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.reading import ReadingCreate, ReadingResponse
from app.services.reading_service import ReadingService

router = APIRouter(
    prefix="/readings",
    tags=["Lecturas"],
)


@router.get(
    "/",
    response_model=list[ReadingResponse],
)
def get_readings(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    service = ReadingService(db)
    return service.get_all(skip, limit)


@router.get(
    "/{reading_id}",
    response_model=ReadingResponse,
)
def get_reading(
    reading_id: int,
    db: Session = Depends(get_db),
):
    service = ReadingService(db)
    return service.get_by_id(reading_id)


@router.post(
    "/",
    response_model=ReadingResponse,
    status_code=201,
)
def create_reading(
    reading: ReadingCreate,
    db: Session = Depends(get_db),
):
    service = ReadingService(db)
    return service.create(reading)


@router.delete(
    "/{reading_id}",
    status_code=204,
)
def delete_reading(
    reading_id: int,
    db: Session = Depends(get_db),
):
    service = ReadingService(db)
    service.delete(reading_id)
    return Response(status_code=204)


@router.get(
    "/filter/date",
    response_model=list[ReadingResponse],
)
def filter_by_date(
    start: datetime = Query(...),
    end: datetime = Query(...),
    db: Session = Depends(get_db),
):
    service = ReadingService(db)
    return service.get_between_dates(start, end)