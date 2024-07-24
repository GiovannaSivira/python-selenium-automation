from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CRT_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    NAVIGATION_SIGN_IN_BTN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    SIGN_IN_BTN =(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)


    def click_cart(self):
        self.wait_and_click(*self.CRT_BTN)



    def click_signin_from_navigation_menu(self):
        self.wait_and_click(*self.SIGN_IN_BTN)
        self.wait_and_click(*self.NAVIGATION_SIGN_IN_BTN)
