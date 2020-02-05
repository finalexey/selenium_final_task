from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Items to buy are presented, but should not be"

    def should_be_text_of_empty_basket(self):
        assert (self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)), \
            "There is no message of empty basket"
