from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click 'add to cart' when you found the product you like")
def click_add_to_cart(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']")
    element.click()
    sleep(4)


@when("Click 'add to cart' under choose options")
def click_add_to_cart_under_choose_options(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='content-wrapper'] button[id*='addToCartButton']")
    element.click()
    sleep(4)


@then("Verify product has been added to cart")
def verify_product_is_added(context):
    expected_text = 'Added to cart'
    element = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")
    actual_text = element[1].text
    assert expected_text == actual_text, f' Expected: {expected_text} Actual: {actual_text}'


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
