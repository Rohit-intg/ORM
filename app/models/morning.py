from app.database import Base
from sqlalchemy import Column, Integer,  Date,ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Morning(Base):
    __tablename__ = "mornings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    confidence_rating = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, onupdate=func.now())
    user = relationship("User", back_populates="mornings")
    activities = relationship("MorningActivity", back_populates="morning")