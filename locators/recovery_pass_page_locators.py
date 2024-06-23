from selenium.webdriver.common.by import By


class RecoveryPassPageLocators:
    enter_button = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    page_recovery_pass = (By.XPATH, ".//h2[text()='Вход']")
    recovery_pass_button = (By.XPATH, ".//a[@href='/forgot-password']")
    recovery_final_button = (By.XPATH, ".//button[text()='Восстановить']")
    email_reset_field = (By.XPATH, ".//input[@name='name']")
    password_reset_field = (By.XPATH, ".//input[@type='password']")
    restore_code_placeholder = (By.XPATH, ".//label[text()='Введите код из письма']")
    open_pass = (By.XPATH,
                 ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    view_pass_button = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
