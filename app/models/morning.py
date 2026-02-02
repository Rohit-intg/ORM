from app.database import Base
from sqlalchemy import Column, Integer,  Date,ForeignKey, TIMESTAMP



class Morning(Base):
    __tablename__ = "mornings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    confidence_rating = Column(Integer)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    