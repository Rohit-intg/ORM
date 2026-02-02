from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://rohikalia:2147%40ROK@localhost:5432/daily_growth"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    bind=engine
)

Base = declarative_base()



