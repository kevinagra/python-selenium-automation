from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDERS_BUTTON = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_BUTTON = (By.ID, 'nav-cart-count')

    def open_main(self):
        self.driver.get("https://www.amazon.com/")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART_BUTTON)

