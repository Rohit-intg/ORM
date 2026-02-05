from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.skill import SkillCreate, SkillResponse
from app.crud.skill import create_skill, get_skills

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/", response_model=SkillResponse)
def create_skill_api(skill: SkillCreate, db: Session = Depends(get_db)):
    return create_skill(db, skill)

@router.get("/", response_model=list[SkillResponse])
def list_skills_api(db: Session = Depends(get_db)):
    return get_skills(db)
