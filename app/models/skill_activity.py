from app.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP,Boolean, Date



class SkillActivity(Base):
    __tablename__ = "skill_activities"
    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    date = Column(Date)
    name = Column(Text, nullable=False)
    completed = Column(Boolean, nullable=False)
    is_priority = Column(Boolean, nullable=False)
    is_habit_to_protect = Column(Boolean, nullable=False)

    minutes_practiced = Column(Integer)

    created_at = Column(TIMESTAMP)
    