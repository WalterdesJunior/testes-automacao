from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, ".btn_inventory")
    BTN_BACK = (By.ID, "back-to-products")

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def add_to_cart(self):
        self.click(self.BTN_ADD_TO_CART)