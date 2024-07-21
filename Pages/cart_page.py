from selenium.webdriver.common.by import By

from Pages.base_page import Page



class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

