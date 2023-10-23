from dotenv import load_dotenv
import os
import allure


@allure.suite('Landing Page')
class TestLandingPage:
    load_dotenv()
    username, password = os.getenv('USERNAME'), os.getenv('PASSWORD')

    @allure.title('Check brand name')
    def test_brand(self, app):
        app.login_page.login(self.username, self.password)
        app.back()
        brand_name = app.landing_page.get_brand_name()
        assert brand_name == 'Zero Bank', app.login_page.make_screenshot()

    @allure.title('Check search input')
    def test_search_input(self, app):
        app.login_page.login(self.username, self.password)
        app.back()
        result = app.landing_page.search_data_by_search_input()

        assert result == 'Search Results:', 'Did not get search Results'
