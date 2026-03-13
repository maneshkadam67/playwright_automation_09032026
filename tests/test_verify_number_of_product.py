from playwright.sync_api import expect

from pages.swag_pages import Swag_Page


def test_first(page):
    swag_page=Swag_Page(page)
    #expect(swag_page.all_products).to_have_count(6)
    assert swag_page.get_number_of_products()==0
