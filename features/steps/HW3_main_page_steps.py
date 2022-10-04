from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLERS = (By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')


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
    element = context.driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
    element.clear()
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    menu = context.driver.find_elements(*HAM_MENU)
    print(menu)

