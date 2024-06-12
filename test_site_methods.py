import yaml
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_invalid_credentials(x_login_selector, x_password_selector, btn_selector, x_error_selector, error_code):
    input_login = site.find_element("xpath", x_login_selector)
    input_login.send_keys("test")
    input_password = site.find_element("xpath", x_password_selector)
    input_password.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_error_selector)
    text = err_label.text
    site.quit()
    assert text == error_code


def test_valid_credentials(x_login_selector, x_password_selector, btn_selector, x_hello_username, x_username):
    input_login = site.find_element("xpath", x_login_selector)
    input_login.clear()
    input_login.send_keys(testdata["username"])
    input_password = site.find_element("xpath", x_password_selector)
    input_password.clear()
    input_password.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()
    login_label = site.find_element("xpath", x_hello_username)
    text = login_label.text
    site.quit()
    assert text == x_username
