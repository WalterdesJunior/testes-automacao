import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCompra:
    def test_adicionar_produto_unico(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=1)
        assert inventory.get_cart_count() == 1

    def test_contagem_do_carrinho_com_multiplos_produtos(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=3)
        inventory.go_to_cart()
        cart = CartPage(logged_in_driver)
        assert cart.get_item_count() == 3

    def test_remover_produto_do_carrinho(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=1)
        inventory.go_to_cart()
        cart = CartPage(logged_in_driver)
        cart.remove_item()
        assert cart.get_item_count() == 0

    def test_ordenar_produtos_por_preco_menor_para_maior(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.sort_by("lohi") # low to high
        prices = inventory.get_all_prices()
        assert prices == sorted(prices)
