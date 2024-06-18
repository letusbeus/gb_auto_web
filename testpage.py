import logging

from selenium.webdriver.common.by import By

from BaseApp import BasePage


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.ID, """create-btn""")
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_NEW_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_NEW_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_NEW_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_CHECK_NEW_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_MESSAGE_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


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
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'Error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]} contains the following error: {text}')
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        logging.info(
            f'\"{text}\" has been found in the field {TestSearchLocators.LOCATOR_HELLO[1]}')
        return text

    def click_new_post_button(self):
        logging.info('The "Create new post" button has been pressed')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_post_title(self, title):
        logging.info(
            f'Title \"{title}\" has been entered into the field {TestSearchLocators.LOCATOR_NEW_POST_TITLE[1]}')
        post_title_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_TITLE)
        post_title_field.clear()
        post_title_field.send_keys(title)

    def enter_post_description(self, description):
        logging.info(
            f'Description \"{description}\" has been entered into the field {TestSearchLocators.LOCATOR_NEW_POST_DESCRIPTION[1]}')
        post_description_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_DESCRIPTION)
        post_description_field.clear()
        post_description_field.send_keys(description)

    def enter_post_content(self, content):
        logging.info(
            f'Content \"{content}\" has been entered into the field {TestSearchLocators.LOCATOR_NEW_POST_CONTENT[1]}')
        post_content_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_CONTENT)
        post_content_field.clear()
        post_content_field.send_keys(content)

    def click_save_new_post_button(self):
        logging.info('The "SAVE" button has been pressed')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_NEW_POST_BTN).click()

    def check_new_post_title(self):
        new_post_title_field = self.find_element(TestSearchLocators.LOCATOR_CHECK_NEW_POST_TITLE, time=2)
        text = new_post_title_field.text
        logging.info(
            f'Title field {TestSearchLocators.LOCATOR_CHECK_NEW_POST_TITLE[1]} contains the following title: {text}')
        return text

    def contact_us_form_request(self):
        logging.info(
            f'"Contact us" form {TestSearchLocators.LOCATOR_CONTACT_US[1]} has been requested')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US).click()

    def enter_user_name(self, name):
        logging.info(
            f'User name \"{name}\" has been entered into the field {TestSearchLocators.LOCATOR_YOUR_NAME_FIELD[1]}')
        user_name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD)
        user_name_field.clear()
        user_name_field.send_keys(name)

    def enter_user_email(self, email):
        logging.info(
            f'User email \"{email}\" has been entered into the field {TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD[1]}')
        user_email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD)
        user_email_field.clear()
        user_email_field.send_keys(email)

    def enter_user_message(self, message):
        logging.info(
            f'User]\'s message \"{message}\" has been entered into the field {TestSearchLocators.LOCATOR_MESSAGE_FIELD[1]}')
        user_message_field = self.find_element(TestSearchLocators.LOCATOR_MESSAGE_FIELD)
        user_message_field.clear()
        user_message_field.send_keys(message)

    def click_contact_us_btn(self):
        logging.info(
            f'"Contact us" button {TestSearchLocators.LOCATOR_CONTACT_US_BTN} has been pressed')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        logging.info(f'Alert text: {alert_text}')
        alert.accept()
        return alert_text
