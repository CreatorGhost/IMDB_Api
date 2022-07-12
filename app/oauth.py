from decouple import config
from jose.jwt import encode , decode
from jose import JWTError
from datetime import datetime, timedelta
import time
from . import *
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException , status
from .schemas import *

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))


def create_jwt_token(user_data:dict):
    # Getting the exipre time
    exp = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Converting the exipre time to a unix timestamp so it can be encoded in the JWT
    exp_time = time.mktime(exp.timetuple())
    
    # Creating a copy of the user data and addinf the exp time to it
    user = user_data.copy()
    user.update({'expiration': exp_time})

    # Encoding the user data with the JWT
    token = encode(user, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt_token(token:str,credentials_expiration):

    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id : str = payload.get('user_id')
        
        if id is None or id != "admin@test.com":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized",headers={'WWW-Authenticate':"Bearer"})
        
        token_data = TokenData(user_id = id)
    except JWTError:
        raise credentials_expiration

    return token_data



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user_token(token : str = Depends(oauth2_scheme)):
    credentials_expiration = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={'WWW-Authenticate':"Bearer"})
    return verify_jwt_token(token, credentials_expiration)