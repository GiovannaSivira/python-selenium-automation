from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CRT_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


    def search(self):
        self.input_text('sunglasses', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)


    def click_cart(self):
        self.click(*self.CRT_BTN)
