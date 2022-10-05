from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLER_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')
BESTSELLERS_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')


@then('Verify Best Sellers column has 5 links')
def verify_link_count(context):
    links = context.driver.find_elements(*BESTSELLERS_LINKS)
    print(links)
    assert len(links) == 5, f'Expected 5 links, but got {len(links)}'

