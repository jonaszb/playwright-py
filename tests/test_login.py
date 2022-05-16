from pages.index import PageObjects
from playwright.sync_api import expect
import pytest
import re

pages = PageObjects()
auth = pytest.users[1]
locked_out_auth = pytest.users[2]
# Test data for invalid login attempts: (username, password, expected_error)
test_data = [("", "", "Epic sadface: Username is required"),
             (auth["username"], "", "Epic sadface: Password is required"),
             (auth["username"], "pass", "Epic sadface: Username and password do not match any user in this service"),
             (locked_out_auth["username"], locked_out_auth["password"], "Epic sadface: Sorry, this user has been locked out.")]


@pytest.fixture
def setup(page, page_objects):
    login_page = page_objects.login(page)
    login_page.navigate()
    yield page
    page.close()


def test_valid_login(setup, page_objects):
    page = setup
    login_page = page_objects.login(page)
    login_page.login(auth['username'], auth['password'])
    expect(page).to_have_url(re.compile(".*inventory"))

@pytest.mark.parametrize("username,password,expected_error", test_data)
def test_invalid_login(setup, page_objects, username, password, expected_error):
    login_page = page_objects.login(setup)
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)
