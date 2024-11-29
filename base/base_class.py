from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class base():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    """Метод вывода коректного url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('url страницы: ' + get_url)

    """Метод сравнения url"""
    def assert_current_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url
        print('url страницы соответсвует документации')

    """Метод поиска элемента на странице"""
    def move_to_elements(self, getter):
        self.action.move_to_element(getter).perform()
        print(f"Опустились к элементу {getter.text}")

    """Метод сравнения содержимого поля"""
    def assert_word(self, word, result):
        value_word = word.get_attribute("value")
        assert value_word == result
        print('Введенный текст/значение соответсвует')

    def execute_script_scrollIntoView(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # self.driver.execute_script("window.scrollTo(0, 200);")

    """Метод пролистывания страницы"""
    def execute_script_down(self):
        self.driver.execute_script("window.scrollTo(0, 1000);")
        print("скрол выполненн")

    """Метод плавной прокрутки страница"""
    def smooth_scrolling_page(self):
        for i in range(0, document.body.scrollHeight, 50):
            self.driver.execute_script(f'window.scrollTo(0, {i})')

    """Метод проверки товара в корзине"""
    def assert_product_card(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")
    """Метод ожидания загрузки элемента"""
    def wait_for_preloader_to_disappear(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, locator))
        )

    """Метод Ожидание загрузки URL"""
    def Waiting_for_URL_to_load(self, url):
        WebDriverWait(self.driver, 10).until(
          EC.url_contains(url)
        )
    """Метод возврата вверх страницы"""
    def return_up_page(self):
        html = self.driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.PAGE_UP)
        print("Вернулись в начало страницы")
















