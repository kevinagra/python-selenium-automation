from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

