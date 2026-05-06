import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def chrome_options():
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    return opts


@pytest.fixture(scope="function")
def driver():
    drv = webdriver.Chrome(options=chrome_options())
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    return driver
