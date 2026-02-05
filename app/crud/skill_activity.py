from sqlalchemy.orm import Session
from app.models.skill_activity import SkillActivity
from app.schemas.skill_activity import SkillActivityCreate

def create_skill_activity(db: Session, activity: SkillActivityCreate):
    db_activity = SkillActivity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity
