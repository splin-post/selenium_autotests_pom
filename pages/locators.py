from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    LOG_FORM = (By.CSS_SELECTOR, '#login_form')   

class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p')

class CartPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.alert>.alertinner')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p')