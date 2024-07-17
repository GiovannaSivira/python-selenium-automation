from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CLICK_CRT =(By.CSS_SELECTOR, "[data-test='@web/CartLink']")

@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    # sleep(6)
    context.driver.wait.until(EC.presence_of_element_located(CLICK_CRT))


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CLICK_CRT).click()

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'
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