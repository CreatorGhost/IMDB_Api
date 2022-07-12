
from ..database import *
from fastapi import FastAPI,Response,HTTPException,status,APIRouter
from ..schemas import AddMovie
from ..oauth import *


router = APIRouter(prefix="/movies",tags=["Movies"])

@router.get("/")
def get_movies():
    return {"movies": get_all_movies()}

@router.get("/{movie_name}")
def get_movie_name(movie_name: str):
    movie = get_movie_by_name(movie_name)
    if len(movie) == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"movie": movie}


@router.get("/n/{n}")
def get_n_movies(n: int):
    return {"movies": show_n_movies(n)}

@router.post("/add_movie",status_code=201)
def create_post(payload:AddMovie,get_current_user: int = Depends(get_current_user_token)):
    movie = payload.dict()
    add_movie(movie)
    return {"message": "Movies added successfully", "Movies": movie["name"]}

# Delete a movie
@router.delete("/{movie_name}")
def delete_movie(movie_name: str,get_current_user: int = Depends(get_current_user_token)):
    movie = get_movie_by_name(movie_name)
    if len(movie) == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    delete_movie_by_name(movie_name)
    return {"message": "Movie deleted successfully", "Movies": movie_name}

# update a movie
@router.put("/{movie_name}")
def update_movie(movie_name: str,payload:AddMovie,get_current_user: int = Depends(get_current_user_token)):
    movie = get_movie_by_name(movie_name)
    if len(movie) == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    update_movie_by_name(movie_name,payload.dict())
    return {"message": "Movie updated successfully", "Movies": movie_name}


# get movies by genre
@router.get("/genre/{genre}")
def movies_by_genre(genre: str):
    return {"movies": get_movies_by_genre(genre)}