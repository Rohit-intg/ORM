from app.database import Base
from sqlalchemy import Column, Integer, Text,ForeignKey, TIMESTAMP, Date



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
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
   
   



