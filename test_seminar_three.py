import logging
import time

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
    testpage.enter_login(username)
    testpage.enter_password(password)
    testpage.click_login_btn()
    assert testpage.get_user_text() == f'Hello, {username}'


def test_create_new_post(browser):
    logging.info('Creating new post')
    testpage = OperationsHelper(browser)
    testpage.click_new_post_button()
    testpage.enter_post_title(title)
    testpage.enter_post_description(description)
    testpage.enter_post_content(content)
    testpage.click_save_new_post_button()
    time.sleep(2)
    assert testpage.check_new_post_title() == title
