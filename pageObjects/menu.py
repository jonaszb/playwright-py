from pageObjects.base import Base


class Menu(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.root_element = page.locator("div.bm-menu-wrap")
        self.menu_items = self.root_element.locator("a.menu-item")
        self.close_icon = self.root_element.locator("#react-burger-cross-btn")

    def get_item_with_text(self, text):
       return self.menu_items.filter(has_text=text) 