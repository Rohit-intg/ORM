from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.morning_activity import (
    MorningActivityCreate,
    MorningActivityResponse,
)
from app.crud.morning_activity import create_morning_activity

router = APIRouter(prefix="/morning-activities", tags=["Morning Activities"])

@router.post("/", response_model=MorningActivityResponse)
def create_morning_activity_api(
    activity: MorningActivityCreate,
    db: Session = Depends(get_db)
):
    return create_morning_activity(db, activity)
