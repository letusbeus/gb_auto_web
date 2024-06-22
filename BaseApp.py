import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru/'

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while opening site')
            start_browsing = None
        return start_browsing

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception('Find element exception')
            element = None
        return element

    def take_screenshot(self, save_path):
        self.driver.save_screenshot(save_path)

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f'Element located at {locator} has no property {property}.')
            return None

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            logging.info(f'Alert text: {alert.text}')
            alert.accept()
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None
