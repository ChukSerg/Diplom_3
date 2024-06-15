import allure

from data import Urls, ConstantsData
from pages.home_page import HomePage


class TestHomePage:
    @allure.title('Тестирование открытие страницы Конструктор')
    def test_constructor_page_open_success(self, driver):
        home_page = HomePage(driver)
        home_page.private_area_transfer()
        home_page.constructor_button_click()
        constructor_title = home_page.get_constructor_title()
        assert constructor_title == ConstantsData.CONSTRUCTOR_TITLE

    @allure.title('Тестирование открытие страницы Лента заказов')
    def test_order_list_page_open_success(self, driver):
        home_page = HomePage(driver)
        home_page.order_list_button_click()
        current_url = driver.current_url
        assert current_url == Urls.ORDER_LIST_URL

    @allure.title('Тестирование открытия окна с деталями ингредиента')
    def test_opening_window_with_ingredient_details(self, driver):
        home_page = HomePage(driver)
        home_page.ingredient_click()
        ingredient_title = home_page.get_ingredient_title()
        assert ingredient_title == ConstantsData.INGREDIENT_TITLE

    @allure.title('Тестирование закрытия Деталей ингредиента при клике на крестик')
    def test_closing_window_ingredient_details(self, driver):
        home_page = HomePage(driver)
        home_page.ingredient_click()
        home_page.close_button_click()
        assert home_page.is_window_ingredient_displayed() is False

    @allure.title('Тестирование увеличения счетчика ингредиента')
    def test_ingredient_counter_increase(self, driver):
        home_page = HomePage(driver)
        home_page.drag_and_drop_ingredient_to_order()
        assert home_page.get_counter_value() == '2'

    @allure.title('Тестирование создания заказа авторизованным пользователем')
    def test_making_order_by_authorized_user(self, driver):
        home_page = HomePage(driver)
        home_page.authorization_enter()
        home_page.drag_and_drop_ingredient_to_order()
        home_page.place_an_order_button_click()
        order_id_text = home_page.get_order_id_text()
        assert order_id_text == ConstantsData.ORDER_ID_TEXT
