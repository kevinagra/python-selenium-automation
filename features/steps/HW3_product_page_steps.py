from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Add to Cart')
def add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()