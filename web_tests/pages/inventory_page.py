from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    BTN_ADD = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_products(self, quantity=1):
        self.wait.until(EC.presence_of_all_elements_located(self.BTN_ADD))
        buttons = self.driver.find_elements(*self.BTN_ADD)
        for btn in buttons[:quantity]:
            btn.click()

    def get_cart_count(self):
        """Retorna a quantidade de itens no carrinho ou 0 se estiver vazio."""
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if len(badges) > 0 else 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, value):
        self.click(self.SORT_CONTAINER)
        option_locator = (By.CSS_SELECTOR, f"option[value='{value}']")
        self.click(option_locator)

    def get_all_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICE)
        return [float(p.text.replace("$", "")) for p in elements]

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAME)
        return [el.text for el in elements]

    def click_item_by_index(self, index=0):
        self.driver.find_elements(*self.ITEM_NAME)[index].click()
