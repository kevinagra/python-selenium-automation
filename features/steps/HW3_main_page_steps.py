from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Clicks on returns & orders link')
def go_to_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@when('Click on empty cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@when('Search for {product}')
def search_product(context, product):
    element = context.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()






