from playwright.sync_api import expect
import pytest

test_data = ["/inventory.html", "/inventory-item.html?id=1", "/cart.html",
             "/checkout-step-one.html", "/checkout-step-two.html", "/checkout-complete.html"]


@pytest.mark.parametrize("url", test_data)
def test_social_links(authpage, page_objects, url):
    base_page = page_objects.base(authpage)
    base_page.navigate(url)

    expect(base_page.linkedin_social).to_have_attribute("href", "https://www.linkedin.com/company/sauce-labs/")
    expect(base_page.facebook_social).to_have_attribute("href", "https://www.facebook.com/saucelabs")
    expect(base_page.twitter_social).to_have_attribute("href", "https://twitter.com/saucelabs")
