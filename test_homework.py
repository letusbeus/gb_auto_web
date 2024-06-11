import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_create_post_and_check_desc(login, test_post_params, test_post_description):
    """
    Создает новый пост с указанными параметрами и проверяет его наличие на сервере по полю «описание».

    Параметры:
    login (str): Токен аутентификации, полученный с помощью функции login.
    test_post_params (dict): Параметры создаваемого поста (title, description, content).
    test_post_description (str): Описание поста, который нужно найти.

    Действия:
    1. Передает в заголовок запроса токен аутентификации, параметры создаваемого поста и описание искомого поста.
    2. Выполняет POST-запрос для создания нового поста.
    3. Проверяет наличие поста на сервере по полю «описание», переданному в заголовок запроса.

    Исключения:
    AssertionError: Если пост с указанным описанием не найден, выводится сообщение об ошибке.
    """
    headers = {"X-Auth-Token": login}
    posts_response = requests.post(data["address"] + "api/posts", params=test_post_params,
                                   headers=headers)
    assert test_post_description in posts_response.json()["description"], (
        'Unfortunately, no such post was found, but you can create one!')
