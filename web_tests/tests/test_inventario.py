import pytest
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage

class TestInventario:
    def test_verificar_detalhes_do_produto(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.click_item_by_index(0)
        
        product = ProductPage(logged_in_driver)
        assert len(product.get_product_name()) > 0