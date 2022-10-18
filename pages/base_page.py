from .locators import LoginPageLocators
from .locators import CartPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_cart(self):
        basket_button = self.browser.find_element(*CartPageLocators.CART_BUTTON)
        basket_button.click()

    def login_user(self, username):
        username_field = self.browser.find_element(*LoginPageLocators.USERNAME_FIELD)
        username_field.click()
        username_field.send_keys(username)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys("secret_sauce")
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
            pass
        except NoSuchElementException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.PRODUCTS_GRID), "User is not authorized"

    def should_not_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_BUTTON), "Error is not visible, but should be"
        assert not self.is_element_present(*LoginPageLocators.PRODUCTS_GRID), \
            "User is authorized, but should not"
