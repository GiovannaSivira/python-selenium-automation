from behave import given, when, then

@given('Open target main page')
def open_target_main_page(context):
    context.app.main_page.open()

@when('Click sign in page')
def open_sign_in_page(context):
    context.app.header.click_signin_from_navigation_menu()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()

@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_tc_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Target Terms and Conditions page is opened')
def verify_target_tc_opened(context):
    context.app.target_terms_and_conditions_page.verify_tc_url()

@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.target_terms_and_conditions_page.close()