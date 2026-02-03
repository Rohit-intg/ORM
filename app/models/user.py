from app.database import Base
from sqlalchemy import Column, Integer, String,  TIMESTAMP



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(String,nullable=False)
    password_hash = Column(String, nullable=False)

    profile_pic_url = Column(String)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)

