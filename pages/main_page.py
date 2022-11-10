from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDERS_BUTTON = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_BUTTON = (By.ID, 'nav-cart-count')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')

    def open_main(self):
        self.driver.get("https://www.amazon.com/")

    def open_kitty_cat_page(self):
        self.driver.get("https://www.amazon.com/gp/product/B074TBCSC8")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def click_cart(self):
        self.click(*self.CART_BUTTON)

    def select_department(self):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value('search-alias=movies-tv')

    # def select_department(self, selection_value):
    #     select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
    #     select.select_by_value(f'search-alias={selection_value}')

