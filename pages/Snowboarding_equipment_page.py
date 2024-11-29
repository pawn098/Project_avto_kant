from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Snowboarding_equipment_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    Snowboards = "//span[text()='Сноуборды']" # Сноуборды
    Snowboard_Boots = "//span[text()='Ботинки для сноуборда']" # Ботинки для сноуборда
    Bindings = "//span[text()='Крепления']" # Крепления
    Splitboarding = "//span[text()='Сплитбординг']" # Сплитбординг
    Snowboard_Kits = "//span[text()='Комплекты сноубордов']" # Комплекты сноубордов
    Masks = "//span[text()='Маски']" # Маски
    Helmets = "//span[text()='Шлемы']" # Шлемы
    Protection = "//span[text()='Защита']" # Защита
    Backpacks = "//span[text()='Рюкзаки']" # Рюкзаки
    Snowboard_Covers = "//span[text()='Чехлы для сноуборда']" # Чехлы для сноуборда
    Boot_Bags = "//span[text()='Сумки для ботинок']" # Сумки для ботинок
    Avalanche_Gear = "//span[text()='Лавинное снаряжение']" # Лавинное снаряжение
    Accessories_and_Spares = "//span[text()='Аксессуары и запчасти']" # Аксессуары и запчасти
    Tools_and_Care = "//span[text()='Инструменты и уход']" # Инструменты и уход

    # getters
    def get_Snowboards(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboards)))
    def get_Snowboard_Boots(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboard_Boots)))
    def get_Bindings(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Bindings)))
    def get_Splitboarding(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Splitboarding)))
    def get_Snowboard_Kits(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboard_Kits)))
    def get_Masks(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Masks)))
    def get_Helmets(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Helmets)))
    def get_Protection(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Protection)))
    def get_Backpacks(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Backpacks)))
    def get_Snowboard_Covers(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboard_Covers)))
    def get_Boot_Bags(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Boot_Bags)))
    def get_Avalanche_Gear(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Avalanche_Gear)))
    def get_Accessories_and_Spares(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Accessories_and_Spares)))
    def get_Tools_and_Care(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Tools_and_Care)))

    # actions
    def click_get_Snowboard_Boots(self):
        self.get_Snowboard_Boots().click()
        print("Перешли в раздел 'Ботинки для сноуборда'")
    def click_get_Snowboards(self):
        self.get_Snowboards().click()
        print("Перешли в раздел 'сноуборды'")
    def click_get_Bindings(self):
        self.get_Bindings().click()
        print("Перешли в раздел 'Крепления'")
    def click_get_Splitboarding(self):
        self.get_Splitboarding().click()
        print("Перешли в раздел 'Сплитбординг'")
    def click_get_Snowboard_Kits(self):
        self.get_Snowboard_Kits().click()
        print("Перешли в раздел 'Комплекты сноубордов'")
    def click_get_Masks(self):
        self.get_Masks().click()
        print("Перешли в раздел 'Маски'")
    def click_get_Helmets(self):
        self.get_Helmets().click()
        print("Перешли в раздел 'Шлемы'")
    def click_get_Protection(self):
        self.get_Protection().click()
        print("Перешли в раздел 'Защита'")
    def click_get_Backpacks(self):
        self.get_Backpacks().click()
        print("Перешли в раздел 'Рюкзаки'")
    def click_get_Snowboard_Covers(self):
        self.get_Snowboard_Covers().click()
        print("Перешли в раздел 'Чехлы для сноуборда'")
    def click_get_Boot_Bags(self):
        self.get_Boot_Bags().click()
        print("Перешли в раздел 'Сумки для ботинок'")
    def click_get_Accessories_and_Spares(self):
        self.get_Accessories_and_Spares().click()
        print("Перешли в раздел 'Аксессуары и запчасти'")
    def click_get_Avalanche_Gear(self):
        self.get_Avalanche_Gear().click()
        print("Перешли в раздел 'Лавинное снаряжение'")
    def click_get_Tools_and_Care(self):
        self.get_Tools_and_Care().click()
        print("Перешли в раздел 'Инструменты и уход'")

    # Methods
    def open_Snowboards(self):
        self.move_to_elements(self.get_Snowboards())
        self.click_get_Snowboards()
        self.Waiting_for_URL_to_load("/catalog/snowboards/snowboard/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/snowboard/")
    def open_Snowboard_Boots(self):
        self.move_to_elements(self.get_Snowboard_Boots())
        self.click_get_Snowboard_Boots()
        self.Waiting_for_URL_to_load("/catalog/snowboards/snowboard-boots/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/snowboard-boots/")
    def open_Bindings(self):
        self.move_to_elements(self.get_Bindings())
        self.click_get_Bindings()
        self.Waiting_for_URL_to_load("/catalog/snowboards/snowboard-bindings/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/snowboard-bindings/")
    def open_Splitboarding(self):
        self.move_to_elements(self.get_Splitboarding())
        self.click_get_Splitboarding()
        self.Waiting_for_URL_to_load("/catalog/snowboards/splitbordy/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/splitbordy/")
    def open_Snowboard_Kits(self):
        self.move_to_elements(self.get_Snowboard_Kits())
        self.click_get_Snowboard_Kits()
        self.Waiting_for_URL_to_load("/catalog/snowboards/snoubord-komplekty/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/snoubord-komplekty/")
    def open_Masks(self):
        self.move_to_elements(self.get_Masks())
        self.click_get_Masks()
        self.Waiting_for_URL_to_load("/catalog/snowboards/maski/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/maski/")
    def open_Helmets(self):
        self.move_to_elements(self.get_Helmets())
        self.click_get_Helmets()
        self.Waiting_for_URL_to_load("/catalog/snowboards/shlemy/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/shlemy/")
    def open_Protection(self):
        self.move_to_elements(self.get_Protection())
        self.click_get_Protection()
        self.Waiting_for_URL_to_load("/catalog/snowboards/zashchita/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/zashchita/")
    def open_Backpacks(self):
        self.move_to_elements(self.get_Backpacks())
        self.click_get_Backpacks()
        self.Waiting_for_URL_to_load("/catalog/snowboards/ryukzaki/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/ryukzaki/")
    def open_Snowboard_Covers(self):
        self.move_to_elements(self.get_Snowboard_Covers())
        self.click_get_Snowboard_Covers()
        self.Waiting_for_URL_to_load("/catalog/snowboards/chekhly-dlya-snouborda/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/chekhly-dlya-snouborda/")
    def open_Boot_Bags(self):
        self.move_to_elements(self.get_Boot_Bags())
        self.click_get_Boot_Bags()
        self.Waiting_for_URL_to_load("/catalog/snowboards/sumki-dlya-botinok/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/sumki-dlya-botinok/")
    def open_Accessories_and_Spares(self):
        self.move_to_elements(self.get_Accessories_and_Spares())
        self.click_get_Accessories_and_Spares()
        self.Waiting_for_URL_to_load("/catalog/snowboards/accessoris/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/accessoris/")
    def open_Avalanche_Gear(self):
        self.move_to_elements(self.get_Avalanche_Gear())
        self.click_get_Avalanche_Gear()
        self.Waiting_for_URL_to_load("/catalog/snowboards/lavinnoe-snaryazhenie/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/lavinnoe-snaryazhenie/")
    def open_Tools_and_Care(self):
        self.move_to_elements(self.get_Tools_and_Care())
        self.click_get_Tools_and_Care()
        self.Waiting_for_URL_to_load("/catalog/snowboards/instruments/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/instruments/")