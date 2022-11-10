from selenium.webdriver.common.by import By
from pages.base_page import Page

class ResultsPage(Page):
    FIRST_RESULT = (By.CSS_SELECTOR, ".a-section.a-spacing-base")
    SELECTED_DEPARTMENT1 = (By.CSS_SELECTOR, '#nav-subnav[data-category="movies-tv"]')
    SELECTED_DEPARTMENT2 = (By.CSS_SELECTOR, '#nav-subnav[data-category="{DEPARTMENT}"]')

    def get_department_locator(self, department: str):
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace('{DEPARTMENT}', department)]

    def click_first_result(self):
        self.click(*self.FIRST_RESULT)

    def verify_department1(self):
        self.wait_for_element_appear(*self.SELECTED_DEPARTMENT1)

    def verify_department2(self, department):
        print('Department -> ', department)
        department_locator = self.get_department_locator(department)
        self.wait_for_element_appear(*SELECTED_DEPARTMENT2)

