from selenium.webdriver.common.by import By
from behave import given, when, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Add to Cart')
def add_to_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()
    context.app.product_page.add_to_cart()


@when('Buy Now button')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#buy-now-button').click()


@when('Click No Thanks, AppleCare')
def add_to_cart(context):
    time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, '#.a-button-input').click()

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]
    assert expected_colors == actual_colors, \
        f' Expected colors {expected_colors} did not match actual {actual_colors}'

