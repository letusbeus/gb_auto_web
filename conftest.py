import pytest
import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    response = requests.post(data["address"] + "gateway/login",
                             data={"username": data["username"], "password": data["password"]})
    return response.json()["token"]


@pytest.fixture()
def test_post_params():
    return {"title": "Post title", "description": "Post description", "content": "Post content"}


@pytest.fixture()
def test_post_description():
    return "Post description"
