from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    BTN_CHECKOUT = (By.ID, "checkout")
    BTN_REMOVE = (By.CSS_SELECTOR, ".cart_button")

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_item(self):
        self.click(self.BTN_REMOVE)

    def proceed_to_checkout(self):
        self.click(self.BTN_CHECKOUT)
