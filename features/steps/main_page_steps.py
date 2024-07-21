from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CLICK_CRT =(By.CSS_SELECTOR, "[data-test='@web/CartLink']")

@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search()
    context.driver.wait.until(EC.presence_of_element_located(CLICK_CRT))


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
   context.app.search_results_page.verify_text()

@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
  context.app.search_results_page.verify_url()

@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")

@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number)  # convert str "6" ==> to int 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links but got {len(links)}'

    # Make sure to always assert len() for multiple elements as shown above
    # because .find_elements() function never fails.
    # This code with incorrect locator will always pass:
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")