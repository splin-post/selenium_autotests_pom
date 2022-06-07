from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_NAME), "Success message is presented, but should not be"



    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_TEXT), 'Empty Basket text info is absent'
