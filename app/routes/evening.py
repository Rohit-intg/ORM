from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.evening import EveningCreate, EveningResponse
from app.crud.evening import create_evening, get_evenings

router = APIRouter(prefix="/evenings", tags=["Evenings"])

@router.post("/", response_model=EveningResponse)
def create_evening_api(evening: EveningCreate, db: Session = Depends(get_db)):
    return create_evening(db, evening)

@router.get("/", response_model=list[EveningResponse])
def list_evenings_api(db: Session = Depends(get_db)):
    return get_evenings(db)
