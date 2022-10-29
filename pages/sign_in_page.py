from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1[contains(@class, 'a-spacing-small')]")

    def verify_signin_text(self):
        expected_result = 'Sign in'
        actual_result = self.driver.find_element(*self.SIGN_IN).text
        assert expected_result == actual_result, f'Expected -> {expected_result}, but got -> {actual_result}'

