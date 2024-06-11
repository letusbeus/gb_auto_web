import requests
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_check_title(login, test_post_title):
    """
    Тестирует наличие поста с указанным заголовком среди опубликованных постов других пользователей с 1-й страницы.

    Параметры:
    login (str): Токен аутентификации, полученный с помощью функции login.
    test_post_title (str): Заголовок поста, который нужно найти.

    Действия:
    1. Передает токен аутентификации в заголовок запроса.
    2. Выполняет GET-запрос для получения списка всех постов, опубликованных другими пользователями, в формате JSON.
    3. Сохраняет заголовки всех постов на странице в список.
    4. Проверяет, содержится ли искомый заголовок в полученном списке.

    Исключения:
    AssertionError: Если заголовок поста не найден в списке, выводится сообщение об ошибке.
    """
    headers = {"X-Auth-Token": login}
    posts_response = requests.get(data["address"] + "api/posts", params={"owner": "notMe", "order": "ASC"}, headers=headers)
    post_titles = [i["title"] for i in posts_response.json()["data"]]
    assert test_post_title in post_titles, 'Unfortunately, no such post was found, but you can create one!'
