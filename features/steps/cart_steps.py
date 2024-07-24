from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when("Click 'add to cart' when you found the product you like")
def click_add_to_cart(context):
    context.app.cart_page.click_add_to_cart()


@when("Click 'add to cart' under choose options")
def click_add_to_cart_under_choose_options(context):
    context.app.cart_page.click_add_to_cart_under_choose_options()


@then("Verify product has been added to cart")
def verify_product_is_added(context):
    context.app.search_results_page.verify_product_is_added()

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()