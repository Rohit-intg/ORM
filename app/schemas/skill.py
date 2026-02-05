from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class SkillResponse(SkillBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
