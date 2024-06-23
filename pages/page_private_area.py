import allure

from pages.base_page import BasePage
from locators.private_area_locators import PrivateAreaPageLocators


class PrivateAreaPage(BasePage):
    @allure.step('Переход в историю заказов')
    def order_history_transfer(self):
        self.button_click(PrivateAreaPageLocators.order_history_link)
        self.wait_open_form(PrivateAreaPageLocators.order_history_list)

    @allure.step('Выход из аккаунта')
    def account_exit(self):
        self.button_click(PrivateAreaPageLocators.button_exit)
        self.wait_open_form(PrivateAreaPageLocators.registration_submit)
