from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCarrinho:
    def test_esvaziar_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(1)
        inventory.go_to_cart()

        cart = CartPage(logged_in_driver)
        cart.remove_item()
        
        # Aguarda até que a lista de itens no carrinho esteja vazia (tamanho 0).
        # O uso de lambda com find_elements é mais resiliente em pipelines de CI.
        assert cart.wait.until(lambda d: len(d.find_elements(*cart.CART_ITEMS)) == 0)
        assert cart.get_item_count() == 0