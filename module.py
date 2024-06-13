import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


class Site:
    def __init__(self, address):
        if browser == "firefox":
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        self.driver.implicitly_wait(3)  # Уменьшено значение implicit wait до 3 секунд
        self.driver.maximize_window()
        self.driver.get(address)

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        elif mode == 'id':
            element = self.driver.find_element(By.ID, path)
        else:
            element = None
        return element

    def wait_for_element(self, mode, path, timeout=10):
        if mode == 'css':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, path))
            )
        elif mode == 'xpath':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
        elif mode == 'id':
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, path))
            )
        else:
            element = None
        return element

    def take_screenshot(self, save_path):
        self.driver.save_screenshot(save_path)

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
