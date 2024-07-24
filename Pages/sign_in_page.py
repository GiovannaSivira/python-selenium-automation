from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_PAGE = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    SIGN_IN_MSSG = (By.CSS_SELECTOR, "h1[class*='sc-fe064f5c-0']")

    def verify_sign_in_form_opened(self):
        self.verify_partial_text('Sign into your Target account', *self.SIGN_IN_MSSG)