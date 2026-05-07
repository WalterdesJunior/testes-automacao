from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCompra:
    def test_adicionar_produto_unico(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=1)
        assert inventory.get_cart_count() == 1

    def test_login_redireciona_para_produtos(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        assert inventory.get_title() == "Products"