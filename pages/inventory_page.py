from pages.base import Base


class InventoryPage(Base):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "/inventory.html"
        # Locators for elements within an item card. Use within the context of an inventory item element.
        self.item_name_locator = "div.inventory_item_name"
        self.item_price_locator = "div.inventory_item_price"
        self.add_to_cart_locator = "button.btn_inventory"

        self.title = self.header_container.locator("span.title")
        self.filter_dropdown = self.header_container.locator("select.product_sort_container")
        self.inventory_container = page.locator("div.inventory_list")
        self.inventory_items = self.inventory_container.locator('div.inventory_item')
        self.item_names = page.locator(self.item_name_locator)
        self.item_prices = page.locator(self.item_price_locator)

    def sort_a_to_z(self):
        self.filter_dropdown.select_option(value="az")

    def sort_z_to_a(self):
        self.filter_dropdown.select_option(value="za")

    def sort_low_to_high(self):
        self.filter_dropdown.select_option(value="lohi")

    def sort_high_to_low(self):
        self.filter_dropdown.select_option(value="hilo")

    def get_all_item_names(self):
        return self.item_names.all_text_contents()

    def get_all_prices(self):
        price_strings = self.item_prices.all_text_contents()
        return [float(price[1:]) for price in price_strings]
