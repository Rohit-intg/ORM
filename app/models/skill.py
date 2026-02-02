from app.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP



class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
   