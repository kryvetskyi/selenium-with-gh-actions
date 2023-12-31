from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import datetime


class BasePage:
    def __init__(self, app):
        self.app = app

    def wait_element_to_be_visible(self, locator, timeout=5):
        return wait(self.app.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_elements_to_be_visible(self, locator, timeout=5):
        return wait(self.app.driver, timeout).until(
            ec.visibility_of_all_elements_located(locator)
        )

    def wait_element_to_be_present(self, locator, timeout=10):
        wait(self.app.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def make_screenshot(self):
        self.app.driver.save_screenshot(f'../screenshots/{datetime.now()}-image.png')
