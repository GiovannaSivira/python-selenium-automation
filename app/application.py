from Pages.cart_page import CartPage
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.base_page import Page
from Pages.search_results_page import SearchResultsPage



class Application:
    def __init__(self, driver):
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.base_page = Page(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)




