from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    BTN_FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    TITLE = (By.CLASS_NAME, "title") # Adicionado o localizador do título da página

    def fill_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.BTN_CONTINUE)
        # Espera explícita pela URL da próxima página
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
        # Espera explícita pelo título da próxima página
        self.wait.until(EC.text_to_be_present_in_element(self.TITLE, "Checkout: Overview"))
        # Espera explícita pelo elemento do total estar visível
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_TOTAL))

    def finish_purchase(self):
        # Espera o botão estar visível e clica
        btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.BTN_FINISH)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()

    def get_confirmation_message(self):
        # Espera até 15s pela mensagem de confirmação
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def get_total(self):
        return self.get_text(self.SUMMARY_TOTAL)