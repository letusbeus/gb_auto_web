import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def good_word():
    return "Привет"


@pytest.fixture()
def bad_word():
    return "Првет"


@pytest.fixture()
def login():
    response = requests.post(data["address"] + "gateway/login",
                             data={"username": data["username"], "password": data["password"]})
    return response.json()["token"]


@pytest.fixture()
def test_post_title():
    return "My firt post"
