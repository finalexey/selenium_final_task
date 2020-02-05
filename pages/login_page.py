from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM)
        password_form = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM)
        password_conf_form = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM_FORM)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON_FORM)

        email_form.send_keys(email)
        password_form.send_keys(password)
        password_conf_form.send_keys(password)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url
        assert 'login' in current_link, 'Invalid link'

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOG_EMAIL_FORM) and
                self.is_element_present(*LoginPageLocators.LOG_PASSWORD_FORM) and
                self.is_element_present(*LoginPageLocators.LOG_BUTTON_FORM)), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REG_EMAIL_FORM) and
                self.is_element_present(*LoginPageLocators.REG_PASSWORD_FORM) and
                self.is_element_present(*LoginPageLocators.REG_PASSWORD_CONFIRM_FORM) and
                self.is_element_present(*LoginPageLocators.REG_BUTTON_FORM)), \
            "Registration form is not presented"
