import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class product_page_snowboard(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators

    size_snowboard = {"см:159W": "//span[text()='см:159W']",
                      "см:162W": "//span[text()='см:162W']",
                      "см:156W": "//span[text()='см:156W']",
                      "см:149": "//span[text()='см:149']",
                      "см:152": "//span[text()='см:152']",
                      "см:157": "//span[text()='см:157']",
                      "см:159": "//span[text()='см:159']"
                      }
    add_card = "(//span[text()='Добавить в корзину'])[2]"


    # getters

    def get_size_snowboard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_snowboard["см:157"])))
    def get_add_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_card)))


    # actions

    def click_get_size_snowboard(self):
        self.get_size_snowboard().click()
        print('Параметр товара размер выбран')
    def click_add_card(self):
        self.get_add_card().click()
        print('Товар добавлен в корзину')


    # Methods
    def adding_product_to_cart(self):
        self.click_get_size_snowboard()
        self.click_add_card()




