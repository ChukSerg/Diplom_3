from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    first_order = (By.XPATH, "(.//a[contains(@href, '/feed/')])[1]")
    orders_details_window = (By.XPATH, ".//p[contains(@class, 'text text_type_digits-default mb-10 mt-5')]")
    order_number_first = (By.XPATH,
                          "(.//a[contains(@href, '/feed/')])[1]//p[@class='text text_type_digits-default']")
    last_order_number = (By.XPATH,
                         "(.//div[contains(@class, 'OrderHistory_textBox')]/"
                         "p[contains(@class, 'text text_type_digits-default')])[last()]")
    order_number_from_pop_up = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    button_closed_order_details = (By.XPATH,
                                   "(.//button[contains(@class, 'Modal_modal__close_modified__3V5XS')])[1]")
    counter_all_time_orders = (By.XPATH, ".//p[contains(text(), 'за все время')]/following-sibling::p")
    order_pre_window = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened__3ISw4')]")
    counter_todat_orders = (By.XPATH, ".//p[contains(text(), 'за сегодня')]/following-sibling::p")
    work_area_empty = (By.XPATH, ".//li[text()='Все текущие заказы готовы!']")
    work_area_order_number = (By.XPATH, "(.//ul[contains(@class, 'OrderFeed_orderListReady')]/li)")
