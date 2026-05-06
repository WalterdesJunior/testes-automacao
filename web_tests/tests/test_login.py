import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    def test_login_com_credenciais_validas(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"

    def test_login_com_senha_errada(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "senha_errada")
        assert "Username and password do not match" in login.get_error_message()

    def test_login_usuario_bloqueado(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        assert "locked out" in login.get_error_message().lower()

    def test_login_sem_credenciais(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("", "")
        assert "Username is required" in login.get_error_message()
