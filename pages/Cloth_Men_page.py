from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cloth_Men_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    filter_price_from = "(//input[@class='Input_input__lvORT'])[1]"  # фильтр по мин. цене
    filter_price_to = "(//input[@class='Input_input__lvORT'])[2]"  # фильтер по макс. цене
    filter_brand = "//div[text()='Бренд']"  # фильтр по бренду
    filter_tip = "//div[text()='Тип']"  # фильтр по типу
    filter_size = "//div[text()='Размер производителя']"  # фильтр по Размер производителя
    filter_season = "//div[text()='Сезон']"  # фильтр по Сезон
    filter_purpose = "//div[text()='Назначение']"  # фильтр по назначению
    filter_year = "//div[text()='Модельный год']"  # фильтр модельному году
    filter_color = "//div[text()='Цвет']"  # фильтр цвету
    filter_stores = "//div[text()='Наличие в магазинах']"  # фильтр по наличию в магазине
    filter_discount = "//div[text()='Наличие скидки']"  # фильтр наличию скидки
    filter_stock = "//div[text()='Акции']"  # фильтр по акции
    checkbox_filter = "//span[@class='Checkbox_checkbox__check__Wrfjf'][1]"
    Search_by_brands = "//input[@placeholder='Поиск по брендам']"
    button_apply = "//span[text()= 'Применить']"
    product_1 = "//div[@data-index='0']"

    # getters

    def get_filter_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_from)))

    def get_filter_price_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_to)))
    def get_filter_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_filter_tip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_tip)))

    def get_filter_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size)))

    def get_filter_purpose(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_purpose)))

    def get_filter_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_year)))

    def get_filter_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_color)))

    def get_filter_stores(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_stores)))

    def get_filter_discount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_discount)))

    def get_filter_stock(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_stock)))

    def get_checkbox_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_filter)))

    def get_Search_by_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Search_by_brands)))

    def get_button_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    # actions

    def filter_price_send_key(self, price1, price2):
        self.move_to_elements(self.get_filter_brand())
        self.get_filter_price_from().clear()
        self.get_filter_price_from().send_keys(price1)
        print("Начальная цена введена")
        self.get_filter_price_to().clear()
        self.get_filter_price_to().send_keys(price2)
        print("Конечная цена введена")

    def filter_brand_click(self):
        self.move_to_elements(self.get_filter_tip())
        self.get_filter_brand().click()
    def filter_tip_click(self):
        self.move_to_elements(self.get_filter_size())
        self.get_filter_tip().click()
    def filter_size_click(self):
        self.move_to_elements(self.get_filter_purpose())
        self.get_filter_size().click()
    def filter_purpose_click(self):
        self.move_to_elements(self.get_filter_year())
        self.get_filter_purpose().click()
    def filter_year_click(self):
        self.move_to_elements(self.get_filter_color())
        self.get_filter_year().click()
    def filter_color_click(self):
        self.move_to_elements(self.get_filter_stores())
        self.get_filter_color().click()

    def filter_stores_click(self):
        self.move_to_elements(self.get_filter_discount())
        self.get_filter_stores().click()

    def filter_discount_click(self):
        self.move_to_elements(self.get_filter_stock())
        self.get_filter_discount().click()

    def filter_stock_click(self):
        self.move_to_elements()

    def checkbox_filter_click(self):
        self.get_checkbox_filter().click()

    def filter_brand_send_key(self, brand):
        self.get_Search_by_brands().send_keys(brand)

    def button_apply_click(self):
        self.get_button_apply().click()

    def product_1_click(self):
        self.move_to_elements(self.get_product_1())
        self.get_product_1().click()

    # Methods
    def close_filters(self):
        self.filter_brand_click()
        self.filter_tip_click()
        self.filter_size_click()
        self.filter_purpose_click()
        self.return_up_page()

    def apply_filter_price(self):
        self.filter_price_send_key("5000", "7000")
        self.move_to_elements(self.get_filter_stock())
        self.filter_brand_click()
        self.filter_brand_send_key("Adidas")
        self.checkbox_filter_click()
        self.filter_brand_click()
        self.button_apply_click()
        self.Waiting_for_URL_to_load(
            "https://www.kant.ru/catalog/clothes/muzhskaya-odezhda/adidas/?filter:price_min=5000&price_max=7000")
        self.wait_for_preloader_to_disappear("Preloader_container__KO_eF")
        self.return_up_page()
        self.product_1_click()
