from pages.base import Base


class LoginPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_field = page.locator('#user-name')
        self.password_field = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('h3[data-test="error"]')

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
