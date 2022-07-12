# IMDB API
## Powered By FastApi

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Introduction
This is a Api that dispalys the data of all the Movies along with its genre and its raatings.Any user can use some of the end points without signing in. User can also create a account and login to do certain tasks but certain operations are just allowed by the admin like adding,deleting and updating movies.

## Features

- Get the list of movies
- Serach for movies [Uses fuzzy logic for searching]
- Get details for specific movie
- Get N number of movies
- Get movies by genre
- Update movie details
- Delete any specific movie
- Add new Movies

### Examples

Fear not! No table with a list of available options comes without a section with examples of how to use them.

| URL                                | Description                              |
| ---------------------------------- | ---------------------------------------- |
| `/image.jpg?w=500`                 | Set width to `500` and use the height from image’s aspect ratio. |
| `/image.jpg?h=250`                 | Set height to `250` and use the width from the image’s aspect ratio. |
| `/image.jpg?w=100&h=100`           | Resize image to `100x100`.               |
| `/image.jpg?w=250&h=250&mode=crop` | Crop image to `250x250` from the center of image. |
| `/image.jpg?w=300&mode=fit`        | Fit image to a width of `300`.           |
| `/image.jpg?w=150&h=100&mode=fit`  | Fit image to `150x100`.                  |
| `/file.pdf`                        | No parameters makes it viewable.         |
| `/file.pdf?download=true`          | Force download of file.                  |

## Pagination
