from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес:
        assert self.browser.current_url.find('login') > 0, 'Page is not LoginPage' 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), 'Login Form is absent'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'Registration form is absent'


    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.E_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self .browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()


         
