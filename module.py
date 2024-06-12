import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Чтобы не скачивать драйвера под конкретный браузер каждый раз вручную, импортируем драйвера для нужных браузеров
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

# Чтобы не скачивать драйвера под конкретный браузер каждый раз вручную... вот эти строки комментируем
# service = Service(testdata["driver_path"])
# options = webdriver.ChromeOptions()


class Site:
    def __init__(self, address):
        # Чтобы не скачивать драйвера под конкретный браузер каждый раз вручную... добавляем эти строки
        if browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        # А эту убираем
        # self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
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
