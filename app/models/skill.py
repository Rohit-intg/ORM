from app.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, onupdate=func.now())
    user = relationship("User", back_populates="skills")
    activities = relationship("SkillActivity", back_populates="skill")