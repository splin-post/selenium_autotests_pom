from sre_constants import SUCCESS
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOG_FORM = (By.CSS_SELECTOR, '#login_form')  
    E_MAIL = (By.CSS_SELECTOR, '#id_registration-email') 
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1') 
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, 'form#register_form>button.btn.btn-lg.btn-primary')
    

class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p')

class CartPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.alert>.alertinner>strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner>p')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")




