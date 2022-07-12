from ..schemas import UserCreate
from ..database import *
from ..utils import *
from fastapi import FastAPI,Response,HTTPException,status ,APIRouter

router = APIRouter(tags=["Users"])



@router.post("/user/sign_up",status_code=201)
def sign_up(user: UserCreate):
    user = user.dict()
    user["password"] = pwd_context.hash(user["password"])
    user_id = add_unique_users(user)
    if not user_id:
        raise HTTPException(status_code=400, detail="User already exists")
    del user_id["password"]
    
    return {"user_id": user_id}

