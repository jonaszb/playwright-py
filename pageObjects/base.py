import pytest


class Base:
    def __init__(self, page):
        self.page = page
        self.url = ""

    def navigate(self):
        self.page.goto(f"{pytest.base_url}{self.url}")
