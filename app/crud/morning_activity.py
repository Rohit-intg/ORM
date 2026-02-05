from sqlalchemy.orm import Session
from app.models.morning_activity import MorningActivity
from app.schemas.morning_activity import MorningActivityCreate

def create_morning_activity(db: Session, activity: MorningActivityCreate):
    db_activity = MorningActivity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
