import logging
import yaml

from selenium.webdriver.common.by import By

from BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, text, desc=None):
        element_name = desc if desc else locator
        logging.debug(f'Send "{text}" to element "{element_name}"')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element "{locator}" not found.')
            return False
        try:
            field.clear()
            field.send_keys(text)
        except:
            logging.exception(f'A locator "{locator}" exception has occurred.')
            return False
        return True

    def click_button(self, locator, desc=None):
        element_name = desc if desc else locator
        button = self.find_element(locator)
        if not button:
            logging.error(f'Button "{element_name}" not found.')
            return False
        try:
            button.click()
        except:
            logging.exception(f'An exception with "{element_name}" click has occurred.')
            return False
        logging.debug(f'Button "{element_name}" has been clicked.')
        return True

    def get_element_text(self, locator, desc=None):
        element_name = desc if desc else locator
        field = self.find_element(locator, time=3)
        if not field:
            logging.error(f'Field "{element_name}" not found.')
            return None
        try:
            text = field.text
            field.click()
        except:
            logging.exception(f'An exception occurred when retrieving the element "{element_name}" text.')
            return None
        logging.debug(f'The element "{element_name}" contains the following text "{text}".')
        return text

    # enter text
    def enter_login(self, login):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], login, desc='Login input')

    def enter_password(self, password):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"], password, desc='Password input')

    def enter_post_title(self, title):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_TITLE"], title, desc='Post title input')

    def enter_post_description(self, description):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_DESCRIPTION"],
                                   description, desc='Post description input')

    def enter_post_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NEW_POST_CONTENT"],
                                   content, desc='Post content input')

    def enter_user_name(self, name):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME_FIELD"], name, desc='Your name input')

    def enter_user_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_FIELD"], email, desc='Your email input')

    def enter_user_message(self, message):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_MESSAGE_FIELD"], message, desc='Your message input')

    # click button
    def click_login_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], desc='Login')

    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], desc='Create post')

    def click_save_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_NEW_POST_BTN"], desc='Save post')

    def contact_us_form_request(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US"], desc='Contact us: open')

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], desc='Contact us: submit')

    # get text
    def get_error_text(self):
        return self.get_element_text(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], desc='Error text')

    def get_hellouser_text(self):
        return self.get_element_text(TestSearchLocators.ids["LOCATOR_HELLO"], desc='Hello text')

    def get_new_post_title(self):
        return self.get_element_text(TestSearchLocators.ids["LOCATOR_CHECK_NEW_POST_TITLE"], desc='Post title text')

    def get_alert(self):
        logging.debug(f'Retrieving alert text')
        text = self.get_alert_text()
        logging.debug(f'Alert text "{text}" has been retrieved.')
        return text
