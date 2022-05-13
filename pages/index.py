from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.menu import Menu
from pages.base import Base

class PageObjects:

    def base(page):
        return Base(page)

    def login_page(page):
        return LoginPage(page)

    def inventory_page(page):
        return InventoryPage(page)
    
    def menu(page):
        return Menu(page)