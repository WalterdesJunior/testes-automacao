from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    BTN_FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.BTN_CONTINUE)

    def finish_purchase(self):
        self.click(self.BTN_FINISH)

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_total(self):
        return self.get_text(self.SUMMARY_TOTAL)
