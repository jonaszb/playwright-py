from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.menu import Menu
from pages.base import Base


class PageObjects:
    def __init__(self):
        self.base = Base
        self.login = LoginPage
        self.inventory = InventoryPage
        self.menu = Menu
