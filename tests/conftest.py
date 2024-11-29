import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    print("Начало теста")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # 2 - блокировать все уведомления
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-infobars")
    options.page_load_strategy = 'normal'
    x = Service()
    driver = webdriver.Chrome(options=options, service=x)
    driver.get('https://www.kant.ru/')
    driver.maximize_window()
    yield driver
    print("Тест завершен")
    # driver.quit()
