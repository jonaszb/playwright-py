from pageObjects.index import PageObjects
from playwright.sync_api import expect
import pytest
import re

auth = pytest.users[1]
locked_out_auth = pytest.users[2]
# Test data for invalid login attempts: (username, password, expected_error)
test_data = [("", "", "Epic sadface: Username is required"),
             (auth["username"], "", "Epic sadface: Password is required"),
             (auth["username"], "pass", "Epic sadface: Username and password do not match any user in this service"),
             (locked_out_auth["username"], locked_out_auth["password"], "Epic sadface: Sorry, this user has been locked out.")]


@pytest.fixture
def setup(page):
    login_page = PageObjects.login_page(page)
    login_page.navigate()
    yield page, login_page
    page.close()


def test_valid_login(setup):
    page, login_page = setup
    login_page.login(auth['username'], auth['password'])
    expect(page).to_have_url(re.compile(".*inventory"))

@pytest.mark.parametrize("username,password,expected_error", test_data)
def test_invalid_login(setup, username, password, expected_error):
    _, login_page = setup
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)
