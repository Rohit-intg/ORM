from app.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP,Boolean


class MorningActivity(Base):
    __tablename__ = "morning_activities"
    id = Column(Integer, primary_key=True, index=True)
    morning_id = Column(Integer, ForeignKey("mornings.id"), nullable=False)


    name = Column(Text, nullable=False)
    completed = Column(Boolean, nullable=False)
    is_priority = Column(Boolean, nullable=False)
    is_habit_to_protect = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
   