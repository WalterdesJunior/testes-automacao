from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCarrinho:
    def test_carrinho_exibe_produto_adicionado(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(1)
        inventory.go_to_cart()
        cart = CartPage(logged_in_driver)
        assert cart.get_item_count() == 1