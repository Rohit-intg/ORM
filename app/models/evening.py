from app.database import Base
from sqlalchemy import Column, Integer, Text,ForeignKey, TIMESTAMP, Date

from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

class Evening(Base):
    __tablename__ = "evenings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    win = Column(Text)
    mistake = Column(Text)
    lesson_learned = Column(Text)
    mood_rating = Column(Integer)
    energy_level = Column(Integer)
    primary_distraction = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, onupdate=func.now())
    # here i am using relatiomships to build connections between the tables.
    user = relationship("User", back_populates="evenings")



