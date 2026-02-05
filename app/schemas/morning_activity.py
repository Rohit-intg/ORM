from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MorningActivityBase(BaseModel):
    morning_id: int
    activity_name: str
    is_completed: bool = False

class MorningActivityCreate(MorningActivityBase):
    pass

class MorningActivityUpdate(BaseModel):
    activity_name: Optional[str] = None
    is_completed: Optional[bool] = None

class MorningActivityResponse(MorningActivityBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
