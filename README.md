# IMDB API
## Powered By FastApi

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduction
This is a Api that dispalys the data of all the Movies along with its genre and its raatings.Any user can use some of the end points without signing in. User can also create a account and login to do certain tasks but certain operations are just allowed by the admin like adding,deleting and updating movies.
I have used mongodb Atlas as a database client and ``JWT Tokens`` are used for `user authentication`


## Features

- Get the list of movies
- Serach for movies [Uses fuzzy logic for searching]
- Get details for specific movie
- Get N number of movies
- Get movies by genre
- Update movie details
- Delete any specific movie
- Add new Movies

## Routes


| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | `/movies`                           | Get the list of all the movies in the Database                   |
| `GET`   | `/movies/{movie_name}`                          | Search Movie by name                      |
| `PUT`    | `/movies/{movie_name}`                          | Update Movie by name.                       |
| `DELETE`  | `/movies/{movie_name}`                          | Delete Movie by name                |
| `GET`   | `/movies/n/{n}`                 | Get N number of movies list                |
| `POST`  | `movies/add_movie`                          | Add new Movie to the database                |
| `GET`   | `/movies/genre/{genre}`                 | Get Movie by Genre                |
| `POST`  | `/user/sign_up`                          | Sign up For a new user account                |
| `GET`   | `/login`                 | Login to perform certain actions          |



## Installation


Install the dependencies and  start the server.

```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

For running the test cases

```sh
python -m pytest -v -s   
```

## License

MIT

