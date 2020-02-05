from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group > a')


class BasketPageLocators:
    ITEMS_TO_BUY = (By.CSS_SELECTOR, '.row > h2')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, 'content_inner, p')


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


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
