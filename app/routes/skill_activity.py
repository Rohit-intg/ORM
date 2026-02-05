from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.skill_activity import (
    SkillActivityCreate,
    SkillActivityResponse,
)
from app.crud.skill_activity import create_skill_activity

router = APIRouter(prefix="/skill-activities", tags=["Skill Activities"])

@router.post("/", response_model=SkillActivityResponse)
def create_skill_activity_api(
    activity: SkillActivityCreate,
    db: Session = Depends(get_db)
):
    return create_skill_activity(db, activity)
  