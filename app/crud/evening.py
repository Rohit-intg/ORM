from sqlalchemy.orm import Session
from app.models.evening import Evening
from app.schemas.evening import EveningCreate

def create_evening(db: Session, evening: EveningCreate):
    db_evening = Evening(**evening.dict())
    db.add(db_evening)
    db.commit()
    db.refresh(db_evening)
    return db_evening

def get_evenings(db: Session):
    return db.query(Evening).all()
