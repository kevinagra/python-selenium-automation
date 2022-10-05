from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Sign in page appears')
def verify_sign_in_page(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1[contains(@class, 'a-spacing-small')]").text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'



@then('Your Amazon Cart is empty')
def cart_is_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").is_displayed(), 'Your Amazon Cart is empty'

