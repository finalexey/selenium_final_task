import time
import pytest
from .pages.locators import ProductPageLocators, MainPageLocators
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'Qq485627fhdfj_'
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):

        link = ProductPageLocators.PAGE_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):

        link = ProductPageLocators.PAGE_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.should_be_adding_product_to_basket()
        page.should_be_same_names_in_basket_and_notification()
        page.should_be_same_prices_in_basket_and_notification()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_adding_product_to_basket()
    page.should_be_same_names_in_basket_and_notification()
    page.should_be_same_prices_in_basket_and_notification()


@pytest.mark.xfail
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


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_adding_product_to_basket()
    time.sleep(1)
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = MainPageLocators.PAGE_LINK
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items_in_basket()
    page.should_be_text_of_empty_basket()
