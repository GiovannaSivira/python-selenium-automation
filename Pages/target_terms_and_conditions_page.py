from selenium.webdriver.common.by import By

from Pages.base_page import Page


class TargetTermsAndConditionsPage(Page):

    def verify_tc_url(self):
        self.verify_partial_url('/terms-conditions/')