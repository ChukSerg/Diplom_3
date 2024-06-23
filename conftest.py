import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, StellarBurgerAuth
from pages.page_private_area import PrivateAreaPage
from locators.private_area_locators import PrivateAreaPageLocators


@pytest.fixture(params=['chrome'])  #'firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(Urls.MAIN_PAGE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def authorized_driver(driver):
    page_authorized = PrivateAreaPage(driver)
    page_authorized.button_click(PrivateAreaPageLocators.private_area_link)
    page_authorized.input_data(PrivateAreaPageLocators.login_email_input, StellarBurgerAuth.EMAIL)
    page_authorized.input_data(PrivateAreaPageLocators.login_password_input, StellarBurgerAuth.PASSWORD)
    page_authorized.button_click(PrivateAreaPageLocators.login_button_submit)
    page_authorized.wait_open_form(PrivateAreaPageLocators.login_expected_text)
    return driver
