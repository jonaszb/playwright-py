from pages.base import Base


class InventoryPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "/inventory.html"
        self.title = self.header_container.locator("span.title")
        self.filter_dropdown = self.header_container.locator("select.product_sort_container")
        self.inventory_container = page.locator("div.inventory_list")
        self.inventory_items = self.inventory_container.locator('div.inventory_item')
