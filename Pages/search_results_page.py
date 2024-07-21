from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'sunglasses' in actual_text, f'Expected sunglasses not in actual {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'sunglasses' in url, f'Expected "sunglasses" not in {url}'



