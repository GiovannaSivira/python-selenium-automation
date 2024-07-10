from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com')

@when('Click Sign in from right side navigation menu')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(6)

@then("Verify Sign In form opened")
def verify_signIn(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()

    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1awz1yh-0']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
    print('Test case passed')
