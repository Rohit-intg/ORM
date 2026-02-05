from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.morning import MorningCreate, MorningResponse
from app.crud.morning import create_morning, get_mornings

router = APIRouter(prefix="/mornings", tags=["Mornings"])

@router.post("/", response_model=MorningResponse)
def create_morning_api(morning: MorningCreate, db: Session = Depends(get_db)):
    return create_morning(db, morning)

@router.get("/", response_model=list[MorningResponse])
def list_mornings_api(db: Session = Depends(get_db)):
    return get_mornings(db)
