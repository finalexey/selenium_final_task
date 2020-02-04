from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):

    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_product_to_basket()
    page.should_be_same_names_in_basket_and_notification()
    page.should_be_same_prices_in_basket_and_notification()
