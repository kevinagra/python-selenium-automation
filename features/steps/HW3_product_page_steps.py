from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Add to Cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@when('Buy Now button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#buy-now-button').click()


@when('Click No Thanks, AppleCare')
def add_to_cart(context):
    time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, '#.a-button-input').click()