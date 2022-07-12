import pymongo
import json
from decouple import config
from random import randint
# Setting up the connection to the database

cluster = pymongo.MongoClient(config("MONGODB_URL"))
db = cluster["IMDB"]
collection = db["Movies"]


users_collection = db["Users"]
# makking sure that the email is unique
users_collection.create_index("email", unique=True)

def add_unique_users(user):
    """
    This function adds a user to the database
    :param user:
    :return:
    """
    user["_id"] = randint(1, 9999999999)
    try:
        users_collection.insert_one(user)
    except pymongo.errors.DuplicateKeyError:
        return False
    return user


def get_user(email):
    """
    This function returns a user by email
    :param email:
    :return:
    """
    return users_collection.find_one({"email": email})




def get_all_movies():
    """
    This function returns a list of all movies in the database
    :return:
    """
    return list(collection.find())



def get_movie_by_name(movie_name):
    """
    This function returns a list of movies that match the search term
    :param movie_name:
    :return: 
    """
    results = collection.aggregate([{
        "$search":{
            "index":"movie_search",
            "text":{
                "query":movie_name,
                "path":"name",
                "fuzzy": {
                    "maxEdits": 2,
                }
            }
        }
    }])

    return list(results)


def delete_movie_by_name(movie_name):
    """
    This function deletes a movie by name
    :param movie_name:
    :return:
    """
    collection.delete_one({"name": movie_name})


def delete_all_movies():
    """
    This function deletes all movies in the database
    :return:
    """
    collection.delete_many({})

def update_movie_by_name(movie_name, new_movie):
    """
    This function updates a movie by name
    :param movie_name:
    :param new_movie:
    :return:
    """
    collection.update_one({"name": movie_name}, {"$set": new_movie})


def show_n_movies(n):
    """
    This function returns the n movies in the database
    :param n:
    :return:
    """
    return list(collection.find().limit(n))


def add_movie(movie):
    """
    This function adds a movie to the database
    :param movie:
    :return:
    """
    movie["_id"] = randint(1, 9999999999)
    collection.insert_one(movie)

# Get movies by genre
def get_movies_by_genre(genre):
    """
    This function returns a list of movies that match the search term
    :param movie_name:
    :return: 
    """
    results = collection.aggregate([{
        "$search":{
            "index":"movie_search",
            "text":{
                "query":genre,
                "path":"genre",
                "fuzzy": {
                    "maxEdits": 2,
                }
            }
        }
    }])

    return list(results)