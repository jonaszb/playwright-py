import pytest
import os
from playwright.sync_api import sync_playwright
from pageObjects.index import PageObjects


def pytest_configure():
    pytest.users = {1: {"username": "standard_user", "password": "secret_sauce"},
                    2: {"username": "locked_out_user", "password": "secret_sauce"},
                    3: {"username": "problem_user", "password": "secret_sauce"},
                    4: {"username": "performance_glitch_user", "password": "secret_sauce"}
                    }
    pytest.base_url = os.getenv('BASE_URL') or "https://www.saucedemo.com"

@pytest.fixture
def authpage(page):
    auth = pytest.users[1]
    login_page = PageObjects.login_page(page)
    login_page.navigate()
    login_page.login(auth["username"], auth["password"])
    yield page
    page.close()
