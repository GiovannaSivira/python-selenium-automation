from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT_ADDED_TO_CART_VERIFICATION = (By.CSS_SELECTOR, 'div[class*="ReactModal"] h2[data-test="modal-drawer-heading"] span[class="h-text-lg"]')

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def verify_product_is_added(self):
        self.verify_text('Added to cart', *self.PRODUCT_ADDED_TO_CART_VERIFICATION)

