from selenium.webdriver.common.by import By


class PrivateAreaPageLocators:
    private_area_link = (By.XPATH, ".//a[@href='/account']")
    login_email_input = (By.XPATH, ".//label[text()='Email']//following-sibling::input")
    login_password_input = (By.XPATH, ".//input[@type='password']")
    login_button_submit = (By.XPATH, ".//button[text()='Войти']")
    login_expected_text = (By.XPATH, ".//button[text()='Оформить заказ']")
    button_exit = (By.XPATH, ".//button[text()='Выход']")
    order_history_link = (By.XPATH, ".//a[@href='/account/order-history']")
    order_history_list = (By.XPATH, ".//ul[contains(@class, 'OrderHistory_profileList')]")
    registration_submit = (By.XPATH, ".//h2[text() = 'Вход']")
