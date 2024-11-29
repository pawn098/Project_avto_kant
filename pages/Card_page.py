from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class card_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    select_all_products = "//*[contains(text(),'Выбрать все')]"
    Place_order = "(//span[contains(text(), 'Оформить заказ')])[2]"


    # getters

    def get_select_all_products(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_all_products)))

    def get_Place_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Place_order)))





    # actions

    def click_get_select_all_products(self):
        self.get_select_all_products().click()
        print("Выбраны все товары в корзине'")
    def click_get_Place_order(self):
        self.get_Place_order().click()
        print("Перешли к оформлению'") # ddd





    # Methods
    def open_select_all_products(self):
        self.Waiting_for_URL_to_load("https://www.kant.ru/basket/")
        self.click_get_select_all_products()
        self.click_get_Place_order()
