from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators, CartPageLocators


class ProductPage(BasePage):
    def should_add_product_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        cart_link.click()

    def should_be_add_to_cart_checks(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()



    def should_be_correct_product_name(self):
        product_page_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        cart_page_name_list = self.browser.find_element(*CartPageLocators.PRODUCT_NAME).text.split()[:-6]
        cart_page_name = ' '.join(cart_page_name_list)
        assert product_page_name == cart_page_name, 'The product name in cart unequal to product name in product page '


    def should_be_correct_product_price(self):
        product_page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_page_price = ''.join(self.browser.find_element(*CartPageLocators.PRODUCT_PRICE).text.split()[-1:])
        assert product_page_price == str(cart_page_price), 'The product price in cart unequal to product price in product page '