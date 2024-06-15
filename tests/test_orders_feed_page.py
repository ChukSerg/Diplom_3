import allure

from pages.orders_feed_page import OrdersFeedPage


class TestOrdersFeedPage:
    @allure.title('Тестирование открытие окна с деталями заказа')
    def test_opening_window_with_order_details(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.order_list_button_click()
        orders_feed_page.first_order_click()
        assert orders_feed_page.is_orders_window_displayed() is True

    @allure.title('Тестирование отображения заказов пользователя на странице Ленты заказов')
    def test_user_order_show_in_order_feed(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.authorization_enter()
        orders_feed_page.make_new_order()
        orders_feed_page.close_details_order_window()
        number = orders_feed_page.get_last_order_number()
        orders_feed_page.order_list_button_click()
        number_window = orders_feed_page.get_order_number()
        assert number_window == number

    @allure.title('Тестирование увеличения счетчика заказов Выполнено за все время')
    def test_check_all_time_counter(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.authorization_enter()
        orders_feed_page.order_list_button_click()
        before_orders = orders_feed_page.get_all_time_counter()
        orders_feed_page.constructor_button_click()
        orders_feed_page.make_new_order()
        orders_feed_page.close_details_order_window()
        orders_feed_page.order_list_button_click()
        after_orders = orders_feed_page.get_all_time_counter()
        assert int(before_orders) < int(after_orders)

    @allure.title('Тестирование увеличения счетчика заказов За сегодня')
    def test_check_today_counter(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.authorization_enter()
        orders_feed_page.order_list_button_click()
        before_orders = orders_feed_page.get_today_counter()
        orders_feed_page.constructor_button_click()
        orders_feed_page.make_new_order()
        orders_feed_page.close_details_order_window()
        orders_feed_page.order_list_button_click()
        after_orders = orders_feed_page.get_today_counter()
        assert int(before_orders) < int(after_orders)

    @allure.title('Тестирование появления нового заказа в разделе В работе')
    def test_check_appearance_new_order_in_work_area(self, driver):
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.authorization_enter()
        orders_feed_page.make_new_order()
        order_number = orders_feed_page.get_new_order_number_in_pop_up()
        orders_feed_page.close_details_order_window()
        orders_feed_page.order_list_button_click()
        assert order_number in orders_feed_page.get_number_order_in_work_area()
