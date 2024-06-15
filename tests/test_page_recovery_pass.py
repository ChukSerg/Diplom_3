import allure

from pages.page_recovery_pass import RecoveryPassPage
from locators.recovery_pass_page_locators import RecoveryPassPageLocators
from data import Urls


class TestPageRecoveryPass:
    @allure.title('Тестирование открытия страницы восстановления пароля')
    def test_opening_page_recovery_pass(self, driver):
        recovery_pass_page = RecoveryPassPage(driver)
        recovery_pass_page.recovery_pass_button_click()
        current_url = driver.current_url
        assert current_url == Urls.RECUVERY_PASS_PAGE_URL

    @allure.title('Тестирование ввода почты и клик по кнопке Восстановить')
    def test_input_email_click_button_restore(self, driver):
        driver.get(Urls.RECUVERY_PASS_PAGE_URL)
        recovery_pass_page = RecoveryPassPage(driver)
        recovery_pass_page.input_email_restore_button_click()
        current_url = driver.current_url
        assert current_url == Urls.RESET_PAGE_URL

    @allure.title('Тестирование отображения символов пароля')
    def test_open_pass_simbols(self, driver):
        driver.get(Urls.RECUVERY_PASS_PAGE_URL)
        recovery_pass_page = RecoveryPassPage(driver)
        recovery_pass_page.input_email_restore_button_click()
        recovery_pass_page.open_pass_simbols()
        assert driver.find_element(*RecoveryPassPageLocators.open_pass).is_displayed()
