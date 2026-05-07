from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCarrinho:
    def test_esvaziar_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(1)
        inventory.go_to_cart()
        # Remove usando o seletor direto, mais estável no CI
        btn = logged_in_driver.find_element(By.CSS_SELECTOR, "button.cart_button")
        btn.click()
        items = logged_in_driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 0