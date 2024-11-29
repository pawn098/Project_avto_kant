from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class catalog_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    Snowboarding_equipment = "//span[text()='Сноуборды']"
    Cloth = "//span[text()='Одежда']"
    Shoes = "//span[text()='Обувь']"
    Alpine_skiing = "//span[text()='Горные лыжи']"
    Cross_country_skiing = "//span[text()='Беговые лыжи']"
    run = "//span[text()='Бег']"
    Tourism = "//span[text()='Туризм']"
    Optics_helmets_protection = "//span[text()='Оптика, шлемы, защита']"
    Backpacks_bags_covers = "//span[text()='Рюкзаки, сумки, чехлы']"
    Bicycles = "//span[text()='Велосипеды']"
    Mountaineering = "//span[text()='Альпинизм']"
    Accessories = "//span[text()='Аксессуары']"
    Scooters = "//span[text()='Самокаты']"
    Rollers = "//span[text()='Ролики']"
    Skateboards_longboards = "//span[text()='Скейтборды, лонгборды']"
    Roller_skis = "//span[text()='Лыжероллеры']"
    Swimming = "//span[text()='Плавание']"
    SUP_Boards_Kayaks = "//span[text()='SUP-Борды и каяки']"



    # getters

    def get_Snowboarding_equipment(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboarding_equipment)))
    def get_Cloth(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Cloth)))
    def get_Shoes(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Shoes)))
    def get_Alpine_skiing(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Alpine_skiing)))
    def get_Cross_country_skiing(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Cross_country_skiing)))
    def get_run(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.run)))
    def get_Tourism(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Tourism)))
    def get_Optics_helmets_protection(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Optics_helmets_protection)))
    def get_Backpacks_bags_covers(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Backpacks_bags_covers)))
    def get_Bicycles(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Bicycles)))
    def get_Mountaineering(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Mountaineering)))
    def get_Accessories(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Accessories)))
    def get_Scooters(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Scooters)))
    def get_Rollers(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Rollers)))
    def get_Skateboards_longboards(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Skateboards_longboards)))
    def get_Roller_skis(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Roller_skis)))
    def get_Swimming(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Swimming)))
    def get_SUP_Boards_Kayaks(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SUP_Boards_Kayaks)))

    # actions

    def click_get_Snowboarding_equipment(self):
        self.move_to_elements(self.get_Snowboarding_equipment())
        self.get_Snowboarding_equipment().click()
        print(f"Перешли в раздел 'Сноуборды'")
    def click_get_Cloth(self):
        self.move_to_elements(self.get_Cloth())
        self.get_Cloth().click()
        print(f"Перешли в раздел 'Одежда'")
    def click_get_Shoes(self):
        self.move_to_elements(self.get_Shoes())
        self.get_Shoes().click()
        print(f"Перешли в раздел 'Обувь'")
    def click_get_Alpine_skiing(self):
        self.move_to_elements(self.get_Alpine_skiing())
        self.get_Alpine_skiing().click()
        print(f"Перешли в раздел 'Горные лыжи'")
    def click_get_Cross_country_skiing(self):
        self.move_to_elements(self.get_Cross_country_skiing())
        self.get_Cross_country_skiing().click()
        print(f"Перешли в раздел 'Беговые лыжи'")
    def click_get_run(self):
        self.move_to_elements(self.get_run())
        self.get_run().click()
        print(f"Перешли в раздел 'Бег'")
    def click_get_Tourism(self):
        self.move_to_elements(self.get_Tourism())
        self.get_Tourism().click()
        print(f"Перешли в раздел 'Туризм'")
    def click_get_Optics_helmets_protection(self):
        self.move_to_elements(self.get_Optics_helmets_protection())
        self.get_Optics_helmets_protection().click()
        print(f"Перешли в раздел 'Оптика, шлемы, защита'")
    def click_get_Backpacks_bags_covers(self):
        self.move_to_elements(self.get_Backpacks_bags_covers())
        self.get_Backpacks_bags_covers().click()
        print(f"Перешли в раздел 'Рюкзаки, сумки, чехлы'")
    def click_get_Bicycles(self):
        self.move_to_elements(self.get_Bicycles())
        self.get_Bicycles().click()
        print(f"Перешли в раздел 'Велосипеды'")
    def click_get_Mountaineering(self):
        self.move_to_elements(self.get_Mountaineering())
        self.get_Mountaineering().click()
        print(f"Перешли в раздел 'Альпинизм'")
    def click_get_Accessories(self):
        self.move_to_elements(self.get_Accessories())
        self.get_Accessories().click()
        print(f"Перешли в раздел 'Аксассуары'")
    def click_get_Scooters(self):
        self.move_to_elements(self.get_Scooters())
        self.get_Scooters().click()
        print(f"Перешли в раздел 'Самокаты'")
    def click_get_Skateboards_longboards(self):
        self.move_to_elements(self.get_Skateboards_longboards())
        self.get_Skateboards_longboards().click()
        print(f"Перешли в раздел 'Скейтборды, лонгборды'")
    def click_get_Rollers(self):
        self.move_to_elements(self.get_Rollers())
        self.get_Rollers().click()
        print(f"Перешли в раздел 'Ролики'")
    def click_get_Roller_skis(self):
        self.move_to_elements(self.get_Roller_skis())
        self.get_Roller_skis().click()
        print(f"Перешли в раздел 'Лыжироллеры'")
    def click_get_Swimming(self):
        self.move_to_elements(self.get_Swimming())
        self.get_Swimming().click()
        print(f"Перешли в раздел 'Плавание'")
    def click_get_SUP_Boards_Kayaks(self):
        self.move_to_elements(self.get_SUP_Boards_Kayaks())
        self.get_SUP_Boards_Kayaks().click()
        print(f"Перешли в раздел 'SUP-Борды и каяки'")


    # Methods
    def open_Snowboarding_equipment(self):
        self.click_get_Snowboarding_equipment()
        self.Waiting_for_URL_to_load("/catalog/snowboards/")
        self.assert_current_url("https://www.kant.ru/catalog/snowboards/")
    def open_Cloth(self):
        self.click_get_Cloth()
        self.Waiting_for_URL_to_load("/catalog/clothes/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/")
    def open_Shoes(self):
        self.click_get_Shoes()
        self.Waiting_for_URL_to_load("/catalog/shoes/")
        self.assert_current_url("https://www.kant.ru/catalog/shoes/")
    def open_Alpine_skiing(self):
        self.click_get_Alpine_skiing()
        self.Waiting_for_URL_to_load("/catalog/alpine-skis/")
        self.assert_current_url("https://www.kant.ru/catalog/alpine-skis/")
    def open_Cross_country_skiing(self):
        self.click_get_Cross_country_skiing()
        self.Waiting_for_URL_to_load("/catalog/skis/")
        self.assert_current_url("https://www.kant.ru/catalog/skis/")
    def open_run(self):
        self.click_get_run()
        self.Waiting_for_URL_to_load("/catalog/sport-running/")
        self.assert_current_url("https://www.kant.ru/catalog/sport-running/")
    def open_Tourism(self):
        self.click_get_Tourism()
        self.Waiting_for_URL_to_load("/catalog/outdoor/")
        self.assert_current_url("https://www.kant.ru/catalog/outdoor/")
    def open_Optics_helmets_protection(self):
        self.click_get_Optics_helmets_protection()
        self.Waiting_for_URL_to_load("/catalog/eyewear-helmet-protector/")
        self.assert_current_url("https://www.kant.ru/catalog/eyewear-helmet-protector/")
    def open_Backpacks_bags_covers(self):
        self.click_get_Backpacks_bags_covers()
        self.Waiting_for_URL_to_load("/catalog/bags-backpacks/")
        self.assert_current_url("https://www.kant.ru/catalog/bags-backpacks/")
    def open_Bicycles(self):
        self.click_get_Bicycles()
        self.Waiting_for_URL_to_load("/catalog/velosipedy/")
        self.assert_current_url("https://www.kant.ru/catalog/velosipedy/")
    def open_Mountaineering(self):
        self.click_get_Mountaineering()
        self.Waiting_for_URL_to_load("/catalog/mountaineering/")
        self.assert_current_url("https://www.kant.ru/catalog/mountaineering/")
    def open_Accessories(self):
        self.click_get_Accessories()
        self.Waiting_for_URL_to_load("/catalog/accessories-list/")
        self.assert_current_url("https://www.kant.ru/catalog/accessories-list/")
    def open_Scooters(self):
        self.click_get_Scooters()
        self.Waiting_for_URL_to_load("/catalog/samokaty/")
        self.assert_current_url("https://www.kant.ru/catalog/samokaty/")
    def open_Rollers(self):
        self.click_get_Rollers()
        self.Waiting_for_URL_to_load("/catalog/roller-blades/")
        self.assert_current_url("https://www.kant.ru/catalog/roller-blades/")
    def open_Skateboards_longboards(self):
        self.click_get_Skateboards_longboards()
        self.Waiting_for_URL_to_load("/catalog/skateboards-longboards/")
        self.assert_current_url("https://www.kant.ru/catalog/skateboards-longboards/")
    def open_Roller_skis(self):
        self.click_get_Roller_skis()
        self.Waiting_for_URL_to_load("/catalog/lyzherollery/")
        self.assert_current_url("https://www.kant.ru/catalog/lyzherollery/")
    def open_Swimming(self):
        self.click_get_Swimming()
        self.Waiting_for_URL_to_load("/catalog/plavanie/")
        self.assert_current_url("https://www.kant.ru/catalog/plavanie/")
    def open_SUP_Boards_Kayaks(self):
        self.click_get_SUP_Boards_Kayaks()
        self.Waiting_for_URL_to_load("/catalog/sup-bording/")
        self.assert_current_url("https://www.kant.ru/catalog/sup-bording/")

