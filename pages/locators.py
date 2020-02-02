from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'


class LoginPageLocators():
    LOG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOG_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_login-password')
    LOG_BUTTON_FORM = (By.CSS_SELECTOR, '[name=login_submit]')
    REG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASSWORD_CONFIRM_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON_FORM = (By.CSS_SELECTOR, '[name=registration_submit]')
    