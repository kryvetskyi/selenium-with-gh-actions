from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LandingPage(BasePage):

    def __init__(self, app):
        super().__init__(app)
        self.app = app

    BRAND_NAME = (By.CSS_SELECTOR, '.brand')
    SEARCH_INPUT = (By.CSS_SELECTOR, '#searchTerm')
    SEARCH_RESULTS_TEXT = (By.CSS_SELECTOR, '.top_offset > h2')

    def get_brand_name(self):
        return self.wait_element_to_be_visible(self.BRAND_NAME).text

    def search_data_by_search_input(self):
        search_box = self.wait_element_to_be_visible(self.SEARCH_INPUT)
        search_box.send_keys('some text')
        search_box.send_keys(Keys.ENTER)

        results_text = self.wait_element_to_be_visible(self.SEARCH_RESULTS_TEXT).text
        return results_text
