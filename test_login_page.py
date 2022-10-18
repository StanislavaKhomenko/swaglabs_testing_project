from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


class TestLoginPage():
    def test_user_can_see_login_page(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()

    def test_user_should_be_able_to_login(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_should_be_able_to_login()
        page.should_be_authorized_user()

    def test_locked_out_user_should_not_be_able_to_log_in(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.locked_out_user_should_not_be_able_to_login()
        page.should_not_be_authorized_user()
