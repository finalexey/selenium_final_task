from .base_page import BasePage, solve_quiz_and_get_code
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_adding_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        # solve_quiz_and_get_code(self)

    def should_be_same_names_in_basket_and_notification(self):
        product_name_main = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        product_name_notification = self.browser.find_element(*ProductPageLocators.NAME_IN_NOTIFICATION)

        assert product_name_main.text == product_name_notification.text, 'Names of products is not the same'

    def should_be_same_prices_in_basket_and_notification(self):
        product_price_main = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MAIN)
        product_price_notification = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_NOTIFICATION)

        assert product_price_main.text == product_price_notification.text, \
            'Prices of product and basket is not the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
