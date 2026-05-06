import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCarrinho:
    def test_esvaziar_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(2)
        inventory.go_to_cart()
        cart = CartPage(logged_in_driver)
        cart.remove_item()
        cart.remove_item()
        assert cart.get_item_count() == 0