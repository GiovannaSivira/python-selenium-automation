from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep

class SignInPage(Page):

    SIGN_IN_PAGE = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    SIGN_IN_MSSG = (By.CSS_SELECTOR, "h1[class*='sc-fe064f5c-0']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_sign_in(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
        # sleep(3)

    def click_target_tc_link(self):
        self.wait_and_click(*self.TC_LINK)


    def verify_sign_in_form_opened(self):
        self.verify_partial_text('Sign into your Target account', *self.SIGN_IN_MSSG)


