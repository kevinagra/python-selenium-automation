from selenium.webdriver.common.by import By
from behave import given, when, then


RESULTS_NAMES = (By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal')
RESULTS_IMAGES = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-square-aspect')


@when('Click on first result')
def click_first_result(context):
    # context.driver.find_element(By.CSS_SELECTOR, ".a-section.a-spacing-base").click()
    context.app.results_page.click_first_result()


# @then('Verify results rows has 62 names')
# def verify_row_name_count(context):
#     names = context.driver.find_elements(*RESULTS_NAMES)
#     print(names)
#     assert len(names) == 62, f'Expected 62 links, but got {len(names)}'
#
#
# @then('Verify results row has {expected_count} images')
# def verify_row_image_count(context, expected_count):
#     images = context.driver.find_elements(*RESULTS_IMAGES)
#     print(images)
#     assert len(images) == expected_count, \
#         f'Expected {expected_count} images, but got {len(images)}

