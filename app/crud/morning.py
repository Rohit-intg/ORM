from sqlalchemy.orm import Session
from app.models.morning import Morning
from app.schemas.morning import MorningCreate

def create_morning(db: Session, morning: MorningCreate):
    db_morning = Morning(**morning.dict())
    db.add(db_morning)
    db.commit()
    db.refresh(db_morning)
    return db_morning

def get_mornings(db: Session):
    return db.query(Morning).all()
  