from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify item(s) line is shown')
def subtotal_item(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()
    assert context.driver.find_element(By.CSS_SELECTOR, "#sc-subtotal-label-buybox").is_displayed(), 'item'

