from dotenv import load_dotenv
import os


class TestLandingPage:
    load_dotenv()
    username, password = os.getenv('USERNAME'), os.getenv('PASSWORD')

    def test_brand(self, app):
        app.login_page.login(self.username, self.password)
        app.back()
        brand_name = app.landing_page.get_brand_name()
        assert brand_name == 'Zero Bank', 'Got incorrect brand name'

    def test_search_input(self, app):
        app.login_page.login(self.username, self.password)
        app.back()
        result = app.landing_page.search_data_by_search_input()

        assert result == 'Search Results:', 'Did not get search Results'


