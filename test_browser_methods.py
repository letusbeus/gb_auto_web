import datetime

import yaml
from module import Site, browser

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_invalid_credentials():
    # тут тестируем получение ошибки 401 при вводе неправильных кредов
    x_login_selector = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_login_selector)
    input1.send_keys("test")
    x_password_selector = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_password_selector)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_error_selector = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_error_selector)
    assert err_label.text == "401", "Oops, looks like you got a NEW error!"


# try:
#     # Печатаем высоту элемента по его селектору
#     css_selector = "span.mdc-text-field__ripple"
#     print(site.get_element_property("css", css_selector, "height"))
#
#     # Получаем свойство color элемента по его xpath
#     xpath = '//*[@id="login"]/div[3]/button/div'
#     print(site.get_element_property("xpath", xpath, "color"))
#
#     # А это еще и скриншот сохранит с временной отметкой
#     # Вот тут получаем временную отметку
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     # тут задаем путь и имя сохраняемого скриншота
#     capture_path = f'D:/gb_auto_web/{browser}_{timestamp}.png'
#     # тут делаем скриншот и сохраняем по указанному пути
#     site.take_screenshot(capture_path)
# finally:
#     site.close()
