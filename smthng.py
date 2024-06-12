from module import Site
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Этот код из презентации демонстрирует, как использовать Selenium для автоматического взаимодействия с веб-страницей
# и ожидания появления элемента.
# Создание экземпляра веб-драйвера: Инициализирует веб-драйвер Firefox.
driver = webdriver.Firefox()
# Открытие веб-страницы: Переходит на указанную веб-страницу.
driver.get("http://somedomain/url_that_delays_loading")
# Ожидание элемента: Ожидает до 10 секунд, пока элемент с ID myDynamicElement не станет присутствовать на странице.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
# Закрытие драйвера: Закрывает веб-драйвер независимо от того, был ли элемент найден или произошла ошибка.
finally:
    driver.quit()


# Этот код демонстрирует использование неявного ожидания в Selenium, что позволяет драйверу ожидать появления
# элементов на странице до указанного времени.
# Импорт библиотеки: Импортирует модуль webdriver из библиотеки Selenium.
from selenium import webdriver
# Создание экземпляра веб-драйвера: Инициализирует веб-драйвер Firefox.
driver = webdriver.Firefox()
# Установка неявного ожидания: Устанавливает неявное ожидание в 10 секунд.
# Это значит, что драйвер будет ждать до 10 секунд для появления элемента перед тем, как выбросить исключение.
driver.implicitly_wait(10)
# Открытие веб-страницы: Переходит на указанную веб-страницу.
driver.get("http://somedomain/url_that_delays_loading")
# Поиск элемента на странице: Ищет элемент на странице по его ID myDynamicElement и сохраняет его в переменную
# myDynamicElement.
myDynamicElement = driver.find_element_by_id("myDynamicElement")

# Получение атрибутов
# Navigate to the url: Переходит на указанную веб-страницу.
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
# Identify the email text box: Ищет элемент на странице по его имени (NAME) и сохраняет его в переменную email_txt.
email_txt = driver._element(By.NAME, "email_input")
# Fetch the value property associated with the textbox: получает значение атрибута value из текстового поля и сохраняет его в переменную value_info.
value_info = email_txt.get_attribute("value")

# Работа с формами
from selenium.webdriver.support.ui import Select
# Выбор элементов в списке: Select используется для работы с элементами <select> на веб-странице.
select = Select(driver.find_element_by_name('name'))
# Методы select_by_index, select_by_visible_text, и select_by_value позволяют выбрать элемент в списке по индексу,
# видимому тексту или значению соответственно.
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

select = Select(driver._element_by_id('id'))
# Метод deselect_all убирает все выбранные элементы в списке (используется для многоразового выбора).
select.deselect_all()

select = Select(driver._element_by_xpath("xpath"))
# Получение всех выбранных опций: all_selected_options возвращает все выбранные элементы в виде списка.
all_selected_options = select.all_selected_options
# Получение всех опций: options возвращает все возможные опции в списке.
options = select.options
# Отправка формы: submit используется для отправки формы, к которой принадлежит элемент.
element.submit()

# Перетаскивание
element = driver._element_by_name("source")
target = driver._element_by_name("target")
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
# Перетаскивание элементов: drag_and_drop используется для перетаскивания элемента source к элементу target.
action_chains.drag_and_drop(element, target)
# Перетаскивание элемента на указанные координаты: drag_and_drop_by_offset используется для перетаскивания элемента на
# определенное смещение (в данном случае 100 пикселей по оси x и 100 пикселей по оси y).
# Используется реже, т.к. координаты могут меняться
drag_and_drop_by_offset(source1, 100, 100)

# Сохранение скриншота: save_screenshot сохраняет скриншот текущей страницы по указанному пути.
capture_path = 'C:/capture/your_desired_filename.png'
driver.save_screenshot(capture_path)
