from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_username_field()
        self.should_be_password_field()
        self.should_be_login_button()

    def should_be_username_field(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), "Username field is absent on the page"

    def should_be_password_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password field is absent on the page"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is absent on the page"

    def user_should_be_able_to_login(self):
        self.login_user("standard_user")

    def locked_out_user_should_not_be_able_to_login(self):
        self.login_user("locked_out_user")
