from pageObjects.login_page import LoginPage
import pytest

auth = pytest.users[1]
login_error = "Epic sadface: Username and password do not match any user in this service"


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


def test_incorrect_password(setup):
    _, loginPage = setup
    loginPage.login(auth['username'], 'wrongpassword')
    assert loginPage.error_message.is_visible()
    assert loginPage.error_message.text_content() == login_error
