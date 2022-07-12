from fastapi import FastAPI,Response,HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel,EmailStr
from typing import Optional
from random import randint
import pymongo
from typing import List, Union
from .database import *
from .utils import *

from .routers import movies,users,auth


app = FastAPI()

app.include_router(movies.router)
app.include_router(users.router)
app.include_router(auth.router)