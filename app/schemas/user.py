from pydantic import BaseModel , constr
from typing import Optional
from datetime import datetime



# for normal common fields validation 

class UserBase(BaseModel):
    first_name:str
    last_name:Optional[str]=None
    email:str

# now i am doing for creating a user input 
class UserCreate(BaseModel):
    password: str 
    



# now i am doing for updating

class UserUpdate(BaseModel):
    first_name:Optional[str]=None
    last_name:Optional[str]=None


# now i am doing for user response

class UserResponse(UserBase):
    id: int
    profile_pic_url: Optional[str] = None
    created_at: datetime
    modified_at: datetime

    class Config:
        from_attributes = True


    
