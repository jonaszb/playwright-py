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


class TestLogin:

    def test_valid_login(self, login_page):
        login_page.login(auth['username'], auth['password'])
        expect(login_page.page).to_have_url(re.compile(".*inventory"))

    @pytest.mark.parametrize("username,password,expected_error", test_data)
    def test_invalid_login(self, login_page, username, password, expected_error):
        login_page.login(username, password)
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_have_text(expected_error)
