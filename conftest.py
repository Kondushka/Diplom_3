import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.feed_orders_page import FeedOrdersPage

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    print("\nstart browser for test..")
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
    
@pytest.fixture()
def main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def feed_orders_page(driver):
    return FeedOrdersPage(driver)
    
@pytest.fixture()
def profile_page(driver):
    return ProfilePage(driver)


