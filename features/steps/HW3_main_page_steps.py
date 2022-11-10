from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLERS = (By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
CUSTOMER_SERVICE = (By.CSS_SELECTOR, "a[href*='nav_cs_customerservice']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_main()


@given('Open Kitty Cat Hoodie page')
def open_amazon(context):
    # context.driver.get("https://www.amazon.com/gp/product/B074TBCSC8")
    context.app.main_page.open_kitty_cat_page()


@when('Clicks on returns & orders link')
def go_to_sign_in_page(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@when('Click Amazon Orders link')
def go_to_sign_in_page(context):
    # context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
    context.app.main_page.click_orders()


@when('Click on empty cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@when('Click on cart icon')
def click_on_cart(context):
    # context.driver.find_element(By.ID, 'nav-cart-count').click()
    context.app.main_page.click_cart()


@when('Search for {product}')
def search_product(context, product):
    # element = context.driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
    # element.clear()
    # element.send_keys(product)
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.main_page.search_product(product)


@when('Click on Best Sellers')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()


@when('Click on Customer Service')
def click_cust_service(context):
    context.driver.find_element(*CUSTOMER_SERVICE).click()


@when('Select Movies & TV department')
def select_department(context):
    context.app.main_page.select_department()


# @when('Select department by value {selection_value}')
# def select_department(context, selection_value):
#     context.app.main_page.select_department(selection_value)


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    menu = context.driver.find_elements(*HAM_MENU)
    print(menu)

