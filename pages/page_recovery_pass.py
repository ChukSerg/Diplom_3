import allure

from pages.base_page import BasePage
from locators.recovery_pass_page_locators import RecoveryPassPageLocators
from data import StellarBurgerAuth


class RecoveryPassPage(BasePage):
    @allure.step('Нажатие на кнопку Восстановить пароль')
    def recovery_pass_button_click(self):
        self.button_click(RecoveryPassPageLocators.enter_button)
        self.wait_open_form(RecoveryPassPageLocators.page_recovery_pass)
        self.button_click(RecoveryPassPageLocators.recovery_pass_button)

    @allure.step('Введение email и нажатие кнопки Восстановить')
    def input_email_restore_button_click(self):
        self.input_data(RecoveryPassPageLocators.email_reset_field, StellarBurgerAuth.EMAIL)
        self.button_click(RecoveryPassPageLocators.recovery_final_button)
        self.wait_open_form(RecoveryPassPageLocators.restore_code_placeholder)

    @allure.step('Открытие символов пароля')
    def open_pass_simbols(self):
        self.wait_open_form(RecoveryPassPageLocators.restore_code_placeholder)
        self.input_data(RecoveryPassPageLocators.password_reset_field, StellarBurgerAuth.PASSWORD)
        self.button_click(RecoveryPassPageLocators.view_pass_button)
