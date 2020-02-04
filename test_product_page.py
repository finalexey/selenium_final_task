import time

import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

#link_offers = ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9']


#@pytest.mark.parametrize('offer', link_offers)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PAGE_LINK
    # link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_adding_product_to_basket()
    page.should_be_same_names_in_basket_and_notification()
    page.should_be_same_prices_in_basket_and_notification()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_product_to_basket()
    time.sleep(1)
    page.should_be_disappeared()
