from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com')

@when('Click Sign in from right side navigation menu')
def click_signin(context):
    context.app.header.click_signin_from_navigation_menu()


@then("Verify Sign In form opened")
def verify_signIn(context):
    context.app.sign_in_page.verify_sign_in_form_opened()


