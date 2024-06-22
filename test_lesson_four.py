import logging
import time
import datetime
import yaml

import testpage
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


def test_invalid_authorization(browser):
    logging.info('Incorrect authorization testing started')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("username")
    testpage.enter_password("password")
    testpage.click_login_btn()
    assert testpage.get_error_text() == "401", "FAIL"


def test_valid_authorization(browser):
    logging.info('Correct authorization testing started')
    testpage = OperationsHelper(browser)
    # del
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_password(password)
    testpage.click_login_btn()
    assert testpage.get_hellouser_text() == f'Hello, {username}'


def test_create_new_post(browser):
    logging.info('Creating new post testing started')
    testpage = OperationsHelper(browser)
    testpage.click_new_post_button()
    testpage.enter_post_title(title)
    testpage.enter_post_description(description)
    testpage.enter_post_content(content)
    testpage.click_save_new_post_button()
    time.sleep(2)
    assert testpage.get_new_post_title() == title


def test_contact_us(browser):
    logging.info('"Contact us" form testing has begun...')
    testpage = OperationsHelper(browser)
    testpage.contact_us_form_request()
    testpage.enter_user_name(name)
    testpage.enter_user_email(email)
    testpage.enter_user_message(message)
    testpage.click_contact_us_btn()
    time.sleep(2)
    alert_text = testpage.get_alert()
    assert alert_text == 'Form successfully submitted', "Alert text does not match expected text."
