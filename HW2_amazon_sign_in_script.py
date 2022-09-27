from selenium import webdriver
from selenium.webdriver.common.by import By

#Use Incognito
c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="/Users/Kevin/Documents/Automation/python-selenium-automation/chromedriver", options=c)
driver.implicitly_wait(0.1)

#Launch URL
driver.get("https://www.amazon.com/")

#Click 'Orders'
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

#Part 1: Verify 'Sign in' page opened, & 'Sign in' header is visible
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']//h1[contains(@class, 'a-spacing-small')]").text
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
print('Test case: Logged out user sees Sign in page when clicking Orders. Part 1/2 passed')

#Part 2: Verify 'Sign in' page opened, & email input field is present
expected_result = driver.find_element(By.XPATH, "//input[@type='email']")
actual_result = driver.find_element(By.XPATH, "//input[@type='email']")
assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
print('Test case: Logged out user sees Sign in page when clicking Orders. Part 2/2 passed')

driver.quit()

"""
Miscellaneous Notes

<a href="/gp/css/order-history?ref_=nav_orders_first" class="nav-a nav-a-2   nav-progressive-attribute" id="nav-orders" tabindex="0">
  #<span class="nav-line-1">Returns</span>
  #<span class="nav-line-2">&amp; Orders<span class="nav-icon nav-arrow"></span></span>


driver = webdriver.Chrome(executable_path='/Users/Kevin/Documents/Automation/python-selenium-automation/chromedriver')

Open https://www.amazon.com
driver.get('https://www.amazon.com/')
"""
