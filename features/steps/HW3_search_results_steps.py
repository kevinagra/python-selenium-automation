from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on first result')
def click_first_result(context):
    context.driver.find_element(By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal").click()

