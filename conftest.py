import pytest
import os
import random
from pages.index import PageObjects


def pytest_configure():
    pytest.users = {1: {"username": "standard_user", "password": "secret_sauce"},
                    2: {"username": "locked_out_user", "password": "secret_sauce"},
                    3: {"username": "problem_user", "password": "secret_sauce"},
                    4: {"username": "performance_glitch_user", "password": "secret_sauce"}
                    }
    pytest.base_url = os.getenv('BASE_URL') or "https://www.saucedemo.com"


@pytest.fixture
def page(page, request):
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}-{random.randint(1000, 10000)}.png")
    page.close()


@pytest.fixture
def authpage(page, page_objects):
    auth = pytest.users[1]
    login_page = page_objects.login(page)
    login_page.navigate()
    login_page.login(auth["username"], auth["password"])
    yield page


@pytest.fixture
def inventory_page(authpage, page_objects):
    inventory_page = page_objects.inventory(authpage)
    inventory_page.navigate()
    yield inventory_page


@pytest.fixture
def login_page(page, page_objects):
    login_page = page_objects.login(page)
    login_page.navigate()
    yield login_page


@pytest.fixture
def base_page(authpage, page_objects):
    base_page = page_objects.base(authpage)
    yield base_page


@pytest.fixture
def page_objects():
    return PageObjects()
