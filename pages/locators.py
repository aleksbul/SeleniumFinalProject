from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    # PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    # PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner > p:nth-child(1) > strong')
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner > p:nth-child(1)')



