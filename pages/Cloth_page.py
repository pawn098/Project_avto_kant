from base.base_class import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cloth_page(base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    Men_clothing = "//span[text()='Мужская одежда']"
    Woman_clothing = "//span[text()='Женская одежда']"
    Children_clothing = "//span[text()='Детская одежда']"
    Accessories_clothing = "//span[text()='Аксессуары']"
    Thermal_underwear = "//span[text()='Термобельё']"
    Softshell_clothing = "//span[text()='Cофтшелл одежда']"
    Membrane_clothing = "//span[text()='Мембранная одежда']"
    Snowboarding_clothing = "//span[text()='Сноубордическая одежда']"
    Alpine_skiing_clothing = "//span[text()='Грнолыжная одежда']"
    Ski_clothing = "//span[text()='Лыжная одежда']"
    Tourist_clothing = "//span[text()='Туристическая одежда']"
    Sports_style = "//span[text()='Спортивный стиль']"
    Running_clothing = "//span[text()='Одежда для бега']"
    Cycling_clothing = "//span[text()='Велоодежда']"
    Impregnations_detergents_clothing = "//span[text()='Пропитки и средства для стирки']"

    # getters
    def get_Men_clothing(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Men_clothing)))
    def get_Woman_clothing(self):
         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Woman_clothing)))
    def get_Children_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Children_clothing)))
    def get_Accessories_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Accessories_clothing)))
    def get_Thermal_underwear(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Thermal_underwear)))
    def get_Softshell_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Softshell_clothing)))
    def get_Membrane_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Membrane_clothing)))
    def get_Snowboarding_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Snowboarding_clothing)))
    def get_Alpine_skiing_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Alpine_skiing_clothing)))
    def get_Ski_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Ski_clothing)))
    def get_Tourist_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Tourist_clothing)))
    def get_Sports_style(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Sports_style)))
    def get_Running_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Running_clothing)))
    def get_Cycling_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Cycling_clothing)))
    def get_Impregnations_detergents_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Impregnations_detergents_clothing)))

    # actions
    def click_get_Men_clothing(self):
        self.get_Men_clothing().click()
        print("Перешли в раздел 'Мужская одежда'")
    def click_get_Woman_clothing(self):
        self.get_Woman_clothing().click()
        print("Перешли в раздел 'Женская одежда'")
    def click_get_Children_clothing(self):
        self.get_Children_clothing().click()
        print("Перешли в раздел 'Детская одежда'")
    def click_get_Accessories_clothing(self):
        self.get_Accessories_clothing().click()
        print("Перешли в раздел 'Аксессуары'")
    def click_get_Thermal_underwear(self):
        self.get_Thermal_underwear().click()
        print("Перешли в раздел 'Термобельё'")
    def click_get_Softshell_clothing(self):
        self.get_Softshell_clothing().click()
        print("Перешли в раздел 'Cофтшелл одежда'")
    def click_get_Membrane_clothing(self):
        self.get_Membrane_clothing().click()
        print("Перешли в раздел 'Мембранная одежда'")
    def click_get_Snowboarding_clothing(self):
        self.get_Snowboarding_clothing().click()
        print("Перешли в раздел 'Сноубордическая одежда'")
    def click_get_Alpine_skiing_clothing(self):
        self.get_Alpine_skiing_clothing().click()
        print("Перешли в раздел 'Грнолыжная одежда'")
    def click_get_Ski_clothing(self):
        self.get_Ski_clothing().click()
        print("Перешли в раздел 'Лыжная одежда'")
    def click_get_Tourist_clothing(self):
        self.get_Tourist_clothing().click()
        print("Перешли в раздел 'Туристическая одежда'")
    def click_get_Sports_style(self):
        self.get_Sports_style().click()
        print("Перешли в раздел 'Спортивный стиль'")
    def click_get_Running_clothing(self):
        self.get_Running_clothing().click()
        print("Перешли в раздел 'Одежда для бега'")
    def click_get_Cycling_clothing(self):
        self.get_Cycling_clothing().click()
        print("Перешли в раздел 'Велоодежда'")
    def click_get_Impregnations_detergents_clothing(self):
        self.get_Impregnations_detergents_clothing().click()
        print("Перешли в раздел 'Пропитки и средства для стирки'")

    # Methods
    def open_Men_clothing(self):
        self.move_to_elements(self.get_Men_clothing())
        self.click_get_Men_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/muzhskaya-odezhda/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/muzhskaya-odezhda/")
    def open_Woman_clothing(self):
        self.move_to_elements(self.get_Woman_clothing())
        self.click_get_Woman_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/zhenskaya-odezhda/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/zhenskaya-odezhda/")
    def open_Children_clothing(self):
        self.move_to_elements(self.get_Children_clothing())
        self.click_get_Children_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/kid-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/kid-clothing/")
    def open_Accessories_clothing(self):
        self.move_to_elements(self.get_Accessories_clothing())
        self.click_get_Accessories_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/other/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/other/")
    def open_Thermal_underwear(self):
        self.move_to_elements(self.get_Thermal_underwear())
        self.click_get_Thermal_underwear()
        self.Waiting_for_URL_to_load("/catalog/clothes/underwear/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/underwear/")
    def open_Softshell_clothing(self):
        self.move_to_elements(self.get_Softshell_clothing())
        self.click_get_Softshell_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/softshell/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/softshell/")
    def open_Membrane_clothing(self):
        self.move_to_elements(self.get_Membrane_clothing())
        self.click_get_Membrane_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/membrana/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/membrana/")
    def open_Snowboarding_clothing(self):
        self.move_to_elements(self.get_Snowboarding_clothing())
        self.click_get_Snowboarding_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/snowboard-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/snowboard-clothing/")
    def open_Alpine_skiing_clothing(self):
        self.move_to_elements(self.get_Alpine_skiing_clothing())
        self.click_get_Alpine_skiing_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/alpine-ski-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/alpine-ski-clothing/")
    def open_Ski_clothing(self):
        self.move_to_elements(self.get_Ski_clothing())
        self.click_get_Ski_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/ski-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/ski-clothing/")
    def open_Tourist_clothing(self):
        self.move_to_elements(self.get_Tourist_clothing())
        self.click_get_Tourist_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/outdoor-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/outdoor-clothing/")
    def open_Sports_style(self):
        self.move_to_elements(self.get_Sports_style())
        self.click_get_Sports_style()
        self.Waiting_for_URL_to_load("/catalog/clothes/sportivnyy-stil/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/sportivnyy-stil/")
    def open_Running_clothing(self):
        self.move_to_elements(self.get_Running_clothing())
        self.click_get_Running_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/run-clothing/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/run-clothing/")
    def open_Cycling_clothing(self):
        self.move_to_elements(self.get_Cycling_clothing())
        self.click_get_Cycling_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/bike-wears/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/bike-wears/")
    def open_Impregnations_detergents_clothing(self):
        self.move_to_elements(self.get_Impregnations_detergents_clothing())
        self.click_get_Impregnations_detergents_clothing()
        self.Waiting_for_URL_to_load("/catalog/clothes/waterproof-treatments/")
        self.assert_current_url("https://www.kant.ru/catalog/clothes/waterproof-treatments/")