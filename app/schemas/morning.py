from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MorningBase(BaseModel):
    title: str
    description: Optional[str] = None

class MorningCreate(MorningBase):
    pass

class MorningUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class MorningResponse(MorningBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
