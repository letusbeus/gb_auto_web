import time


def test_valid_credentials(site, testdata, x_login_selector, x_password_selector, btn_login_selector, x_hello_username):
    # Проверка авторизации
    input_login = site.wait_for_element("xpath", x_login_selector)
    input_login.clear()
    input_login.send_keys(testdata["username"])
    input_password = site.wait_for_element("xpath", x_password_selector)
    input_password.clear()
    input_password.send_keys(testdata["password"])
    btn_login = site.wait_for_element("css", btn_login_selector)
    btn_login.click()
    login_label = site.wait_for_element("xpath", x_hello_username)
    text = login_label.text.split(" ")
    assert text[-1] == testdata["username"], "Authorization failed"


def test_create_post(site, testdata, create_btn_selector, x_input_post_title, x_input_post_description,
                     x_input_post_content, btn_save_post_selector, check_new_post_title):
    # Проверка создания нового поста
    btn_create_post = site.wait_for_element("id", create_btn_selector)
    btn_create_post.click()
    input_title = site.wait_for_element("xpath", x_input_post_title)
    input_title.clear()
    input_title.send_keys(testdata["title"])
    input_description = site.wait_for_element("xpath", x_input_post_description)
    input_description.clear()
    input_description.send_keys(testdata["description"])
    input_content = site.wait_for_element("xpath", x_input_post_content)
    input_content.clear()
    input_content.send_keys(testdata["content"])
    btn_save_post = site.wait_for_element("xpath", btn_save_post_selector)
    btn_save_post.click()
    time.sleep(testdata["sleep_time"])
    post_label = site.wait_for_element("xpath", check_new_post_title)
    text = post_label.text
    assert text == testdata["title"], "Post creation failed"
