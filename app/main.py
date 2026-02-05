from fastapi import FastAPI
from app.database import engine, Base
from app.models import *
from app.schemas.user import UserCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/test-user")
def test_user(user: UserCreate):
    return user


from fastapi import FastAPI

from app.routes.user import router as user_router
from app.routes.skill import router as skill_router
from app.routes.morning import router as morning_router
from app.routes.evening import router as evening_router
from app.routes.morning_activity import router as morning_activity_router
from app.routes.skill_activity import router as skill_activity_router

app = FastAPI()

app.include_router(user_router)
app.include_router(skill_router)
app.include_router(morning_router)
app.include_router(evening_router)
app.include_router(morning_activity_router)
app.include_router(skill_activity_router)
