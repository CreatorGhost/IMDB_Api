from fastapi import FastAPI,Response,HTTPException,status ,APIRouter,Depends
from ..utils import verify
from ..schemas import *
from ..database import get_user
from ..oauth import *
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Users"])



@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends()):
    

    password = user.password
    user_id = user.username
    if user_id is None :
        raise HTTPException(status_code=403, detail="Please provide valid credentials")
    
    user_password = get_user(user_id)["password"]

    if not verify(password, user_password):
        raise HTTPException(status_code=403, detail="Please provide valid credentials")

    token = create_jwt_token(user_data={"user_id": user_id})
    return {"token": token,"token_type": "bearer"}