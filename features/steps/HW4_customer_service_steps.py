from selenium.webdriver.common.by import By
from behave import given, when, then

#(By.CSS_SELECTOR, "input[name='email'][type='email'][maxlength='128']")

ALL_HELP_HEADER = (By.XPATH, "//*[@class='fs-heading bolded']")
CUSTOMER_SERVICE = (By.XPATH, "//*[@class='fs-heading bolded']")
CUSTOMER_SERVICE_LINKS = (By.CSS_SELECTOR, ".issue-card-wrapper")
HELP_LIBRARY = (By.XPATH, "//*[@class='fs-heading bolded']")
HELP_SEARCH_BAR = (By.CSS_SELECTOR, '.a-search.a-span12')
HELP_TOPICS_SECTION = (By.CSS_SELECTOR, '.help-topics-list-wrapper')


@then('Customer Service page shows')
def cust_serv_page(context):
    assert context.driver.find_element(*CUSTOMER_SERVICE).is_displayed(), 'Welcome to Amazon Customer Service'.text


@then('Verify 9 Customer Service links')
def verify_link_count(context):
    links = context.driver.find_elements(*CUSTOMER_SERVICE_LINKS)
    print(links)
    assert len(links) == 9, f'Expected 9 links, but got {len(links)}'


@then('Verify - Search our help library')
def help_library(context):
    assert context.driver.find_element(*HELP_LIBRARY).is_displayed(), 'Search our help library'.text


@then('Verify - help search bar is present')
def help_search_bar(context):
    expected_result = context.driver.find_element(*HELP_SEARCH_BAR)
    actual_result = context.driver.find_element(*HELP_SEARCH_BAR)
    assert expected_result == actual_result, f'Expected-> {expected_result}, but got-> {actual_result}'


@then('Verify - All help topics')
def help_library(context):
    assert context.driver.find_element(*ALL_HELP_HEADER).is_displayed(), 'All help topics'.text


@then('Verify - help topics section exists')
def help_topics_section(context):
    expected_result = context.driver.find_element(*HELP_TOPICS_SECTION)
    actual_result = context.driver.find_element(*HELP_TOPICS_SECTION)
    assert expected_result == actual_result, f'Expected-> {expected_result}, but got-> {actual_result}'

