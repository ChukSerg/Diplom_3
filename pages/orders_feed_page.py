import allure

from locators.orders_feed_page_locators import OrdersFeedPageLocators
from locators.private_area_locators import PrivateAreaPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step('Клик на заказ')
    def first_order_click(self):
        self.wait_open_form(OrdersFeedPageLocators.first_order)
        self.button_click(OrdersFeedPageLocators.first_order)

    @allure.step('Проверка наличия окна заказа')
    def is_orders_window_displayed(self):
        self.wait_open_form(OrdersFeedPageLocators.orders_details_window)
        return self.element_displayed(OrdersFeedPageLocators.orders_details_window)

    @allure.step('Получение номера заказа')
    def get_last_order_number(self):
        self.button_click(PrivateAreaPageLocators.private_area_link)
        self.wait_open_form(PrivateAreaPageLocators.button_exit)
        self.button_click(PrivateAreaPageLocators.order_history_link)
        self.wait_open_form(PrivateAreaPageLocators.order_history_list)
        return self.get_text(OrdersFeedPageLocators.last_order_number)

    @allure.step('Закрыть окно заказа')
    def close_details_order_window(self):
        self.button_click(OrdersFeedPageLocators.button_closed_order_details)

    @allure.step('Получение номера заказа в окне Ленты заказов')
    def get_order_number(self):
        self.wait_open_form(OrdersFeedPageLocators.order_number_first)
        return self.get_text(OrdersFeedPageLocators.order_number_first)

    @allure.step('Создание заказа')
    def make_new_order(self):
        self.drag_and_drop_ingredient_to_order()
        self.place_an_order_button_click()
        self.closed_order_pre_window()

    @allure.step('Получение счетчика заказов за все время')
    def get_all_time_counter(self):
        self.wait_open_form(OrdersFeedPageLocators.counter_all_time_orders)
        return self.get_text(OrdersFeedPageLocators.counter_all_time_orders)

    @allure.step('Ожидание закрытия предварительного окна заказа')
    def closed_order_pre_window(self):
        self.wait_open_form(OrdersFeedPageLocators.order_pre_window)
        self.wait_for_closed_form(OrdersFeedPageLocators.order_pre_window)

    @allure.step('Получение счетчика заказов за сегодня')
    def get_today_counter(self):
        self.wait_open_form(OrdersFeedPageLocators.counter_todat_orders)
        return self.get_text(OrdersFeedPageLocators.counter_todat_orders)

    @allure.step('Получение номера заказа во всплывающем окне')
    def get_new_order_number_in_pop_up(self):
        self.wait_open_form(OrdersFeedPageLocators.order_number_from_pop_up)
        return self.get_text(OrdersFeedPageLocators.order_number_from_pop_up)

    def get_number_order_in_work_area(self):
        self.wait_open_form(OrdersFeedPageLocators.work_area_empty)
        self.wait_for_closed_form(OrdersFeedPageLocators.work_area_empty)
        return self.get_text(OrdersFeedPageLocators.work_area_order_number)
