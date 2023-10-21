from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, app):
        super().__init__(app)
        self.app = app

    LOGIN_INPUT = (By.CSS_SELECTOR, "#user_login")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#user_password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#signin_button")
    KEEP_SIGN_IN_CHECKBOX = (By.CSS_SELECTOR, "#user_remember_me")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit']")
    LOGIN_ERROR_MSG = (By.CSS_SELECTOR, ".alert")
    LOGGED_IN_USERNAME = (By.CSS_SELECTOR, ".dropdown-toggle")
    LOGOUT = (By.CSS_SELECTOR, '#logout_link')

    def login(self, username, password):
        self.app.open_main_page()
        self.wait_element_to_be_visible(self.SIGN_IN_BUTTON).click()
        self.wait_element_to_be_visible(self.LOGIN_INPUT).send_keys(username)
        self.wait_element_to_be_visible(self.PASSWORD_INPUT).send_keys(password)
        self.wait_element_to_be_visible(self.KEEP_SIGN_IN_CHECKBOX).click()
        self.wait_element_to_be_visible(self.SUBMIT_BUTTON).click()

    def logout(self):
        self.wait_elements_to_be_visible(self.LOGGED_IN_USERNAME)[1].click()
        self.wait_element_to_be_visible(self.LOGOUT).click()

    def get_error_msg_text(self):
        error_message_element = self.wait_element_to_be_visible(self.LOGIN_ERROR_MSG)
        return error_message_element.text

    def get_logged_username(self):
        return self.wait_elements_to_be_visible(self.LOGGED_IN_USERNAME)[1].text
