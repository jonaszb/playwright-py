from pageObjects.inventory_page import InventoryPage
from pageObjects.login_page import LoginPage
from pageObjects.menu import Menu

class PageObjects:

    def login_page(page):
        return LoginPage(page)

    def inventory_page(page):
        return InventoryPage(page)
    
    def menu(page):
        return Menu(page)