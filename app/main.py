from fastapi import FastAPI
from app.database import engine, Base
from app.models import *
from app.schemas.user import UserCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/test-user")
def test_user(user: UserCreate):
    return user