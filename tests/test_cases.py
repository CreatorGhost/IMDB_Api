import pytest
import requests
from fastapi.testclient import TestClient
from app.main import app
from random import randint
from jose.jwt import decode
from app.schemas import * 
from decouple import config


client = TestClient(app)

num = randint(1, 9999999999)
email = "test"+str(num)+"@example.com"

def test_movie_search():
    res = client.get("movies/Star Wars")
    assert res.status_code == 200
    assert len(res.json()['movie']) >= 1

def test_create_user():
    res = client.post("user/sign_up",json={"email":email,"password":"12345"})
    assert res.status_code == 201
    assert res.json()["user_id"]['email'] == email


def test_create_duplicate_user():
    res = client.post("user/sign_up",json={"email":email,"password":"12345sa"})
    assert res.status_code == 400
    assert res.json()["detail"] == "User already exists"



def test_login_user():
    res = client.post(
        "/login", data={"username": email, "password": "12345"})
    login_res = Token(**res.json())
    payload = decode(login_res.token,
                         config("SECRET_KEY"), algorithms=[config("ALGORITHM")])
    id = payload.get("user_id")
    assert id == email
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
    return res.json()


def test_login_route():
    token = test_login_user()
    print(token)
    

def test_login_wrong_user():
    res = client.post(
        "/login", data={"username": email, "password": "xs12345"})
    assert res.status_code == 403
    assert res.json()["detail"] == "Please provide valid credentials"
