import allure

from pages.page_private_area import PrivateAreaPage
from data import Urls


class TestPrivateAreaPage:
    @allure.title('Проверка перехода в личный кабинет по клику на Личный кабинет')
    def test_transfer_to_private_area(self, authorized_driver):
        private_area_page = PrivateAreaPage(authorized_driver)
        private_area_page.private_area_transfer_with_authorization()
        current_url = private_area_page.get_current_url()
        assert current_url == Urls.PRIVATE_AREA_URL

    @allure.title('Проверка возможности просмотра заказов')
    def test_transfer_to_order_history(self, authorized_driver):
        private_area_page = PrivateAreaPage(authorized_driver)
        private_area_page.private_area_transfer_with_authorization()
        private_area_page.order_history_transfer()
        current_url = private_area_page.get_current_url()
        assert current_url == Urls.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_account_exit(self, authorized_driver):
        private_area_page = PrivateAreaPage(authorized_driver)
        private_area_page.private_area_transfer_with_authorization()
        private_area_page.account_exit()
        current_url = private_area_page.get_current_url()
        assert current_url == Urls.LOGIN_URL
