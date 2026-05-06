import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCompra:
    def test_fluxo_completo_compra(self, logged_in_driver):
        """E2E: login → adiciona produtos → checkout → confirmação."""
        driver = logged_in_driver

        # Adiciona 2 produtos ao carrinho
        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"
        inventory.add_products(quantity=2)
        assert inventory.get_cart_count() == 2

        # Verifica carrinho
        inventory.go_to_cart()
        cart = CartPage(driver)
        assert cart.get_title() == "Your Cart"
        assert cart.get_item_count() == 2

        # Preenche dados de checkout
        cart.proceed_to_checkout()
        checkout = CheckoutPage(driver)
        checkout.fill_info("Teste", "Silva", "12345-000")

        # Valida total e finaliza
        total = checkout.get_total()
        assert "Total:" in total

        checkout.finish_purchase()
        assert checkout.get_confirmation_message() == "Thank you for your order!"

    def test_adicionar_produto_unico(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=1)
        assert inventory.get_cart_count() == 1

    def test_carrinho_reflete_produtos_adicionados(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_products(quantity=3)
        inventory.go_to_cart()
        cart = CartPage(logged_in_driver)
        assert cart.get_item_count() == 3
