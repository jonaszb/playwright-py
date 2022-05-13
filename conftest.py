import pytest
import os
from playwright.sync_api import sync_playwright


def pytest_configure():
    pytest.users = {1: {"username": "standard_user", "password": "secret_sauce"},
                    2: {"username": "locked_out_user", "password": "secret_sauce"},
                    3: {"username": "problem_user", "password": "secret_sauce"},
                    4: {"username": "performance_glitch_user", "password": "secret_sauce"}
                    }
    pytest.base_url = os.getenv('BASE_URL') or "https://www.saucedemo.com"
