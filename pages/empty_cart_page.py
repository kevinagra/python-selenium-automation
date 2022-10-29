from selenium.webdriver.common.by import By
from pages.base_page import Page

class EmptyCartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")

    def verify_cart_empty(self):
        assert self.driver.find_element(*self.EMPTY_CART).is_displayed(), 'Your Amazon Cart is empty'

