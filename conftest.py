import pytest
import yaml
from module import Site


@pytest.fixture(scope='module')
def testdata():
    with open('testdata.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def site(testdata):
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.quit()


@pytest.fixture()
# Находит поле ввода логина
def x_login_selector():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
# Находит поле ввода пароля
def x_password_selector():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
# Находит код ошибку при попытке авторизации при вводе некорректных данных
def x_error_selector():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
# Находит кнопку "LOGIN"
def btn_login_selector():
    return """button"""


@pytest.fixture()
# Возвращает код 401
def error_code():
    return """401"""


@pytest.fixture()
# Возвращает сообщение пользователя при провале теста
def error_msg():
    return """Oops, looks like you got a NEW error!"""


@pytest.fixture()
# Находит текст "Hello {username}" в правом верхнем углу после успешной авторизации
def x_hello_username():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
# Находит кнопку создания нового поста
def create_btn_selector():
    return """create-btn"""


@pytest.fixture()
# Находит поле ввода заголовка нового поста
def x_input_post_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
# Находит поле ввода описания нового поста
def x_input_post_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
# Находит поле ввода контента нового поста
def x_input_post_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
# Находит поле ввода даты публикации нового поста
def x_input_post_data():
    return """//*[@id="create-item"]/div/div/div[5]/div/div/label/input"""


@pytest.fixture()
# Находит кнопку сохранения нового поста
def btn_save_post_selector():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
# Находит заголовок созданного поста
def check_new_post_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""
