import pytest
import os
from dotenv import load_dotenv

from pages.application import Application
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def app():
    load_dotenv()
    base_url = os.getenv('BASE_URL')

    options = Options()
    options.headless = True

    fixture = Application(
        webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),
                                               options=options)), base_url)

    yield fixture

    fixture.quit()

