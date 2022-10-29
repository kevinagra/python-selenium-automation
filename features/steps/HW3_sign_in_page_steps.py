from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Sign in page appears')
def verify_sign_in_page(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1[contains(@class, 'a-spacing-small')]").text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'


@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    # expected_result = 'Sign in'
    # actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1[contains(@class, 'a-spacing-small')]").text
    # assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.sign_in_page.verify_signin_text()


@then('Your Amazon Cart is empty')
def cart_is_empty(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").is_displayed(), 'Your Amazon Cart is empty'


@then('Verify Your Shopping Cart is empty - text present')
def cart_is_empty(context):
    # assert context.driver.find_element(By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty").is_displayed(), 'Your Amazon Cart is empty'
    context.app.empty_cart_page.verify_cart_empty()

