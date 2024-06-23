import allure

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    @allure.step('Получение заголовка Конструктора')
    def get_constructor_title(self):
        element = self.get_text(HomePageLocators.constructor_title)
        return element

    @allure.step('Клик на ингредиент')
    def ingredient_click(self):
        self.button_click(HomePageLocators.first_ingredients_details)

    @allure.step('Получение заголовка Деталей ингредиента')
    def get_ingredient_title(self):
        return self.get_text(HomePageLocators.ingredient_title)

    @allure.step('Клик на крестике')
    def close_button_click(self):
        self.button_click(HomePageLocators.button_closed_ingredient_details)

    @allure.step('Проверка наличия окна ингредиента')
    def is_window_ingredient_displayed(self):
        self.wait_for_closed_form(HomePageLocators.ingredient_title)
        return self.element_displayed(HomePageLocators.ingredient_title)

    @allure.step('Получение значения счетчика ингредиента')
    def get_counter_value(self):
        return self.get_text(HomePageLocators.first_ingredient_counter)

    @allure.step('Получение текста идентификатора заказа')
    def get_order_id_text(self):
        return self.get_text(HomePageLocators.order_id_confirmation)
