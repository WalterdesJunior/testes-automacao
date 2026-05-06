import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


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
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Driver já autenticado no SauceDemo."""
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    return driver


# Page fixtures para reuso nos testes
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(logged_in_driver):
    return InventoryPage(logged_in_driver)


@pytest.fixture
def cart_page(logged_in_driver):
    return CartPage(logged_in_driver)


@pytest.fixture
def checkout_page(logged_in_driver):
    return CheckoutPage(logged_in_driver)
