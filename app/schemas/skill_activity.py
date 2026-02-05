from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SkillActivityBase(BaseModel):
    skill_id: int
    activity_name: str
    duration_minutes: Optional[int] = None

class SkillActivityCreate(SkillActivityBase):
    pass

class SkillActivityUpdate(BaseModel):
    activity_name: Optional[str] = None
    duration_minutes: Optional[int] = None

class SkillActivityResponse(SkillActivityBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
