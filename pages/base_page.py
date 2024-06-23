import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import StellarBurgerAuth
from locators.home_page_locators import HomePageLocators
from locators.private_area_locators import PrivateAreaPageLocators


class BasePage:
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку {button_xpath}')
    def button_click(self, button_xpath):
        self.driver.find_element(*button_xpath).click()

    @allure.step('Ожидаем открытие раздела {form_title}')
    def wait_open_form(self, form_title):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(form_title))

    @allure.step('Ожидаем закрытие раздела {form_title}')
    def wait_for_closed_form(self, form_title):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element(form_title))

    @allure.step('Вводим данные в форму')
    def input_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Переход в личный кабинет неавторизованного пользователя')
    def private_area_transfer(self):
        self.button_click(PrivateAreaPageLocators.private_area_link)
        self.wait_open_form(PrivateAreaPageLocators.registration_submit)

    @allure.step('Переход в личный кабинет авторизованного пользователя')
    def private_area_transfer_with_authorization(self):
        self.button_click(PrivateAreaPageLocators.private_area_link)
        self.wait_open_form(PrivateAreaPageLocators.button_exit)

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверка наличия элемента')
    def element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    @allure.step('Перетаскивание элемента из {source} в {target}')
    def drag_and_drop_element(self, source, target):
        source_place = self.driver.find_element(*source)
        target_place = self.driver.find_element(*target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_place, target_place)
        action.perform()

    @allure.step('Перенос ингредиента в корзину заказа')
    def drag_and_drop_ingredient_to_order(self):
        self.drag_and_drop_element(HomePageLocators.first_ingredients_details,
                                   HomePageLocators.section_order_basket)

    @allure.step('Клик на кнопку Оформить заказ')
    def place_an_order_button_click(self):
        self.button_click(HomePageLocators.place_an_order_button)

    @allure.step('Клик на Ленту заказов')
    def order_list_button_click(self):
        self.button_click(HomePageLocators.button_orders_feed)

    @allure.step('Прокрутка до нужного элемента {locator}')
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_open_form(locator)

    @allure.step('Клик на Конструктор')
    def constructor_button_click(self):
        self.button_click(HomePageLocators.button_construct)
        self.wait_open_form(HomePageLocators.constructor_header)

    @allure.step('Получение url адреса')
    def get_current_url(self):
        return self.driver.current_url
