from pageObjects.login_page import LoginPage
import pytest

auth = pytest.users[1]
locked_out_auth = pytest.users[2]
# Test data for invalid login attempts: (username, password, expected_error)
test_data = [("", "", "Epic sadface: Username is required"),
             (auth["username"], "", "Epic sadface: Password is required"),
             (auth["username"], "pass", "Epic sadface: Username and password do not match any user in this service"),
             (locked_out_auth["username"], locked_out_auth["password"], "Epic sadface: Sorry, this user has been locked out.")]


@pytest.fixture
def setup(page):
    loginPage = LoginPage(page)
    loginPage.navigate()
    yield page, loginPage
    page.close()


def test_valid_login(setup):
    page, loginPage = setup
    loginPage.login(auth['username'], auth['password'])
    assert "inventory.html" in page.url

@pytest.mark.parametrize("username,password,expected_error", test_data)
def test_invalid_login(setup, username, password, expected_error):
    _, loginPage = setup
    loginPage.login(username, password)
    assert loginPage.error_message.is_visible()
    assert loginPage.error_message.text_content() == expected_error
