from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'


class LoginPageLocators:
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOG_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_login-password')
    LOG_BUTTON_FORM = (By.CSS_SELECTOR, '[name=login_submit]')
    REG_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASSWORD_CONFIRM_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON_FORM = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE_MAIN = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, '#messages :first-child > div > strong')
    PRODUCT_PRICE_NOTIFICATION = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child > .alertinner')
