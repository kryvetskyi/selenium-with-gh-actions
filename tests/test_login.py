import allure
from dotenv import load_dotenv
from helper.generate_user import generate
import pytest
import os

load_dotenv()


@pytest.mark.parametrize('username, password', [
    (os.getenv('USERNAME'), os.getenv('PASSWORD')),
    generate()
])
@allure.title('Check login')
def test_login_with_valid_creds(app, username, password):
    if username == os.getenv('USERNAME'):
        app.login_page.login(username, password)
        app.back()
        assert app.login_page.get_logged_username() == os.getenv('USERNAME'), 'Error message is present but should not'
        app.login_page.logout()

    else:
        app.login_page.login(username, password)
        assert app.login_page.get_error_msg_text() == 'Login and/or password are wrong.', 'Incorrect message'
