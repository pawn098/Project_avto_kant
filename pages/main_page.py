from selenium.webdriver import ActionChains

from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class main_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    pop_up = "//div[@class='popmechanic-close']"
    catalog = "//a[@class='Header_catalogBtn__3urTC']"
    card = "//div[@class='Header_dropdownMenuContainer__0AMAG']"

    # getters

    def get_pop_up(self):
        return WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, self.pop_up)))
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))
    def get_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card)))

    # actions

    def click_get_pop_up(self):
        self.get_pop_up().click()
        print("Закрылось всплывающее окно")
    def click_get_catalog(self):
        self.get_catalog().click()
        print("Перешли в каталог")
    def click_get_card(self):
        self.get_card().click()
        print("Перешли в корзину")

    # Methods
    def open_catalog_page(self):
        self.click_get_pop_up()
        self.click_get_catalog()
        self.Waiting_for_URL_to_load("/catalog/")
        self.get_current_url()
        self.assert_current_url('https://www.kant.ru/catalog/')

    def open_card(self):
        self.click_get_card()
        self.Waiting_for_URL_to_load("/basket/")
        self.get_current_url()
        self.assert_current_url('https://www.kant.ru/basket/')





