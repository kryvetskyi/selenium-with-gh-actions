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
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    fixture = Application(
        webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options), base_url)

    yield fixture

    fixture.quit()
