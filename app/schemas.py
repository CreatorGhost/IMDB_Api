from pydantic import BaseModel,EmailStr

from typing import List, Union,Optional



class UserCreate(BaseModel):
    email: EmailStr
    password: str

class AddMovie(BaseModel):
    popularity : int
    director : str
    genre : List[str] = []
    imdb_score : float
    name : str


class Token(BaseModel):
    token: str
    token_type: str


class TokenData(BaseModel):
    user_id: str
    # set is admin as Optional
    is_admin: Optional[bool] = False