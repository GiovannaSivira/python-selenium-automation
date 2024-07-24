from selenium.webdriver.common.by import By

from Pages.base_page import Page



class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CLK_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CLK_ADD_TO_CART_UNDER_CHOOSE_OPTION = (By.CSS_SELECTOR, "div[data-test='content-wrapper'] button[id*='addToCartButton']")

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)


    def click_add_to_cart(self):
        self.wait_and_click(*self.CLK_ADD_TO_CART_BTN)

    def click_add_to_cart_under_choose_options(self):
        self.wait_and_click(*self.CLK_ADD_TO_CART_UNDER_CHOOSE_OPTION)
