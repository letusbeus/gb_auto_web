import pytest
import yaml

from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


@pytest.fixture()
def x_login_selector():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_password_selector():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_error_selector():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector():
    return """button"""


@pytest.fixture()
def error_code():
    return """401"""


@pytest.fixture()
def error_msg():
    return """Oops, looks like you got a NEW error!"""


@pytest.fixture()
def x_hello_username():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def x_username():
    return f'Hello, {testdata["username"]}'
