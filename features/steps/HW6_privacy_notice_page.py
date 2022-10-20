from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

