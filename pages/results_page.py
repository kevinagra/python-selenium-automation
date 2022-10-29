from selenium.webdriver.common.by import By
from pages.base_page import Page

class ResultsPage(Page):
    FIRST_RESULT = (By.CSS_SELECTOR, ".a-section.a-spacing-base")

    def click_first_result(self):
        self.click(*self.FIRST_RESULT)

