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
        
        # Aguarda até que o item desapareça do DOM para evitar flutuabilidade no pipeline
        assert cart.wait.until(EC.invisibility_of_element_located(cart.CART_ITEMS))
        assert cart.get_item_count() == 0