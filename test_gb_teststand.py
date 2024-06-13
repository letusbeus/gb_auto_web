import time

import yaml
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_valid_credentials(x_login_selector, x_password_selector, btn_login_selector, x_hello_username,
                           create_btn_selector, x_input_post_title, x_input_post_description, x_input_post_content,
                           btn_save_post_selector, check_new_post_title):
    asserts = []
    input_login = site.find_element("xpath", x_login_selector)
    input_login.clear()
    input_login.send_keys(testdata["username"])
    input_password = site.find_element("xpath", x_password_selector)
    input_password.clear()
    input_password.send_keys(testdata["password"])
    btn_login = site.find_element("css", btn_login_selector)
    btn_login.click()
    login_label = site.find_element("xpath", x_hello_username)
    text = login_label.text.split(" ")
    asserts.append(True if text[-1] == testdata["username"] else False)
    btn_create_post = site.find_element("id", create_btn_selector)
    btn_create_post.click()
    time.sleep(testdata["sleep_time"])
    input_title = site.find_element("xpath", x_input_post_title)
    input_title.clear()
    input_title.send_keys(testdata["title"])
    input_description = site.find_element("xpath", x_input_post_description)
    input_description.clear()
    input_description.send_keys(testdata["description"])
    input_content = site.find_element("xpath", x_input_post_content)
    input_content.clear()
    input_content.send_keys(testdata["content"])
    btn_save_post = site.find_element("xpath", btn_save_post_selector)
    btn_save_post.click()
    time.sleep(testdata["sleep_time"])
    post_label = site.find_element("xpath", check_new_post_title)
    text = post_label.text
    asserts.append(True if text == testdata["title"] else False)
    site.quit()
    print(*asserts)
    assert all(asserts), "FAIL"
