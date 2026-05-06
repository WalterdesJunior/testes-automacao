from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    BTN_ADD = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_first_product(self):
        self.click(self.BTN_ADD)

    def add_products(self, quantity=1):
        buttons = self.driver.find_elements(*self.BTN_ADD)
        for btn in buttons[:quantity]:
            btn.click()

    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
