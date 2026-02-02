from app.database import Base
from sqlalchemy import Column, Integer, String,  TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String,nullable=False)
    password_hash = Column(String, nullable=False)
    phone_number = Column(Integer)
    profile_pic_url = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    modified_at = Column(TIMESTAMP, onupdate=func.now())

# here i am using relatiomships to build connections between the tables.

    mornings = relationship("Morning", back_populates="user")
    evenings = relationship("Evening", back_populates="user")
    skills = relationship("Skill", back_populates="user")