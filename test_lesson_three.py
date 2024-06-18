from testpage import OperationsHelper
import logging


def test_invalid_authorization(browser):
    logging.info('Authorization testing started')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("username")
    testpage.enter_password("password")
    testpage.click_login_btn()
    testpage.get_error_text()
    assert testpage.get_error_text() == "401", "FAIL"
