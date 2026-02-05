from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EveningBase(BaseModel):
    title: str
    description: Optional[str] = None

class EveningCreate(EveningBase):
    pass

class EveningUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class EveningResponse(EveningBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
