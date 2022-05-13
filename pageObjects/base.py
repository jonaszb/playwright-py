import pytest


class Base:
    def __init__(self, page):
        self.page = page
        self.url = ""
        self.header_container = page.locator("#header_container")
        self.menu_icon = self.header_container.locator("#react-burger-menu-btn")
        self.cart_icon = self.header_container.locator("#shopping_cart_container")


    def navigate(self, url=""):
        self.page.goto(f"{pytest.base_url}{url or self.url}")
