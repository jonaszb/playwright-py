from playwright.sync_api import expect
import pytest

auth = pytest.users[1]
test_data = ["/inventory.html", "/inventory-item.html?id=1", "/cart.html",
             "/checkout-step-one.html", "/checkout-step-two.html", "/checkout-complete.html"]
menu_rows = ["ALL ITEMS", "LOGOUT", "ABOUT", "RESET APP STATE"]


class TestMenu:

    def test_no_nav_menu_on_login(self, login_page):
        expect(login_page.menu_icon).not_to_be_visible()

    @pytest.mark.parametrize("url", test_data)
    def test_after_login(self, authpage, page_objects, url):
        page = authpage
        base_page = page_objects.base(page)
        menu = page_objects.menu(page)

        base_page.navigate(url)
        expect(base_page.menu_icon).to_be_visible()
        expect(menu.root_element).not_to_be_visible()
        base_page.menu_icon.click()
        expect(menu.root_element).to_be_visible()
        expect(menu.menu_items).to_have_count(4)
        for expected_item in menu_rows:
            expect(menu.get_item_with_text(expected_item)).to_be_visible()
        menu.close_icon.click()
        expect(menu.root_element).not_to_be_visible()
