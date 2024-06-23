import logging
import time
import datetime
import yaml
import atexit
from sender import send_report
from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
username = testdata["username"]
password = testdata["password"]
title = testdata["title"]
description = testdata["description"]
content = testdata["content"]
name = testdata["name"]
email = testdata["email"]
message = testdata["message"]
path = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'


# Вызывает функцию отправки отчета на почту после выполнения всех тестов
atexit.register(send_report)


def test_invalid_authorization(browser):
    testname = 'Incorrect authorization'
    logging.info(f'"{testname}": test RUNNING')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("username")
    testpage.enter_password("password")
    testpage.click_login_btn()
    assert testpage.get_error_text() == "401", "FAIL"
    logging.info(f'"{testname}": test PASSED')


def test_valid_authorization(browser):
    testname = 'Correct authorization'
    logging.info(f'"{testname}": test RUNNING')
    testpage = OperationsHelper(browser)
    testpage.enter_login(username)
    testpage.enter_password(password)
    testpage.click_login_btn()
    assert testpage.get_hellouser_text() == f'Hello, {username}'
    logging.info(f'"{testname}": test PASSED')


def test_create_new_post(browser):
    testname = 'Creating new post'
    logging.info(f'"{testname}": test RUNNING')
    testpage = OperationsHelper(browser)
    testpage.click_new_post_button()
    testpage.enter_post_title(title)
    testpage.enter_post_description(description)
    testpage.enter_post_content(content)
    testpage.click_save_new_post_button()
    time.sleep(2)
    assert testpage.get_new_post_title() == title
    logging.info(f'"{testname}": test PASSED')


def test_contact_us_form(browser):
    testname = '"Contact us" form'
    logging.info(f'"{testname}": test RUNNING')
    testpage = OperationsHelper(browser)
    testpage.contact_us_form_request()
    testpage.enter_user_name(name)
    testpage.enter_user_email(email)
    testpage.enter_user_message(message)
    testpage.click_contact_us_btn()
    time.sleep(2)
    alert_text = testpage.get_alert()
    assert alert_text == 'Form successfully submitted', "Alert text does not match expected text."
    logging.info(f'"{testname}": test PASSED')
