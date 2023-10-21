from pages.base_page import BasePage
from pages.landing_page import LandingPage
from pages.login_page import LoginPage


class Application:
    def __init__(self, driver, base_url):
        self.login_page = LoginPage(self)
        self.base_page = BasePage(self)
        self.landing_page = LandingPage(self)
        self.base_url = base_url
        self.driver = driver

    def open_main_page(self):
        self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()
