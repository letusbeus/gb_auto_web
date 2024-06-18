from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")


class OperationsHelper(BasePage):
    def enter_login(self, login):
        logging.info(f'Login \"{login}\" has been sent to login field {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login)

    def enter_password(self, password):
        logging.info(
            f'Password \"{password}\" has been sent to password field {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}')
        password_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_btn(self):
        logging.info('The "LOGIN" button has been pressed')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'Error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]} contains the following error: {text}')
        return text
