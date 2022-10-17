class TestInventorySorting:

    def test_a_to_z_sorting(self, inventory_page):
        inventory_page.sort_a_to_z()
        names = inventory_page.get_all_item_names()
        assert all(names[i] <= names[i+1] for i in range(len(names) - 1))

    def test_z_to_a_sorting(self, inventory_page):
        inventory_page.sort_z_to_a()
        names = inventory_page.get_all_item_names()
        assert all(names[i] >= names[i+1] for i in range(len(names) - 1))

    def test_low_to_high_sorting(self, inventory_page):
        inventory_page.sort_low_to_high()
        prices = inventory_page.get_all_prices()
        assert all(prices[i] <= prices[i+1] for i in range(len(prices) - 1))

    def test_high_to_low_sorting(self, inventory_page):
        inventory_page.sort_high_to_low()
        prices = inventory_page.get_all_prices()
        assert all(prices[i] >= prices[i+1] for i in range(len(prices) - 1))
