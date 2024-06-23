from selenium.webdriver.common.by import By


class HomePageLocators:
    button_construct = (By.XPATH, ".//p[text()='Конструктор']")
    constructor_header = (By.XPATH, './/h1[text()="Соберите бургер"]')
    constructor_title = (By.XPATH, ".//h1[contains(@class, 'text_type_main-large')]")
    button_orders_feed = (By.XPATH, ".//p[text()='Лента Заказов']")
    order_list_header = (By.XPATH, './/h1[text()="Соберите бургер"]')
    order_list_title = (By.XPATH, ".//p[contains(@class, 'text_type_main-large')]")
    first_ingredients_details = (By.XPATH, "(.//a[contains(@href, '/ingredient/')])[1]") #".//img[@alt='tick animation']")
    ingredient_title = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    button_closed_ingredient_details = (By.XPATH,
                                        "(.//button[contains(@class, 'Modal_modal__close_modified__3V5XS')])[1]")
    section_order_basket = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    first_ingredient_counter = (By.XPATH,
                                "(.//a[contains(@href, '/ingredient/')])[1]//p[contains(@class, 'counter__num')]")
    place_an_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    order_id = (By.XPATH, ".//img[@alt='tick animation']")
    order_id_confirmation = (By.XPATH, "//p[text()='идентификатор заказа']")
