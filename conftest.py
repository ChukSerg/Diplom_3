import pytest
from selenium import webdriver

from data import Urls


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
