import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls, StellarBurgerAuth
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
    driver.find_element(*PrivateAreaPageLocators.private_area_link).click()
    driver.find_element(*PrivateAreaPageLocators.login_email_input).send_keys(StellarBurgerAuth.EMAIL)
    driver.find_element(*PrivateAreaPageLocators.login_password_input).send_keys(StellarBurgerAuth.PASSWORD)
    driver.find_element(*PrivateAreaPageLocators.login_button_submit).click()
    WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(PrivateAreaPageLocators.login_expected_text))
    return driver
