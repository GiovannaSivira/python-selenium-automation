from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
#
# @given('Open Target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com')
#
# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
#     sleep(6)
#
# @then("Verify 'Your cart is empty' message is shown")
# def verify_cart_is_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']").text
#     print(actual_text)
#     assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
#     print('Test case passed')