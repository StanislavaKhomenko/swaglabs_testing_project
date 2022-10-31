from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest


class TestCheckoutFlow():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.saucedemo.com"
        page = LoginPage(browser, link)
        page.open()
        page.user_should_be_able_to_login()
        page.should_be_authorized_user()
        page = ProductPage(browser, browser.current_url)
        page.add_product_to_cart_item_2()
        page.should_be_sorting_by_price_from_low_to_high_and_adding_first_option_to_cart()
        page.go_to_cart()
        page = CartPage(browser, browser.current_url)
        page.should_be_checkout_button()
        page.should_be_clickable_checkout_button()


class TestUserShouldBeAbleToReachFirstStepOfCheckout(TestCheckoutFlow):
    def test_user_should_see_first_step_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.should_be_first_step_of_checkout()

    def test_user_should_see_cancel_button_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.should_be_cancel_button_of_checkout()

    def test_user_should_be_able_to_left_checkout_and_see_selected_items_in_cart(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_cancel_button_of_checkout()
        page.should_be_correct_quantity_of_selected_items()
        page.should_be_selected_item_2_in_cart()


class TestUserShouldBeAbleToInteractWithFirstStepOfCheckout(TestCheckoutFlow):
    def test_user_should_be_able_to_fill_first_name_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_first_name_field_of_checkout()

    def test_user_should_see_correct_value_of_first_name_field_of_checkout_after_filling_it(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_first_name_field_of_checkout()
        page.should_be_correct_value_of_first_name_field_of_checkout()

    def test_user_should_be_able_to_fill_last_name_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_last_name_field_of_checkout()

    def test_user_should_see_correct_value_of_last_name_field_of_checkout_after_filling_it(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_last_name_field_of_checkout()
        page.should_be_correct_value_of_last_name_field_of_checkout()

    def test_user_should_be_able_to_fill_postal_code_field_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()

    def test_user_should_see_correct_value_of_postal_code_field_of_checkout_after_filling_it(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()
        page.should_be_correct_value_of_postal_code_field_of_checkout()

    def test_user_should_see_continue_button_on_the_first_step_of_checkout(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.should_be_continue_button_of_checkout()

    def test_user_should_see_error_message_by_clicking_on_continue_button_with_no_data_entered(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_continue_button_of_checkout()
        page.should_be_error_message_when_user_tries_to_pass_first_step_of_checkout_without_data()


class TestUserShouldBeAbleToReachSecondStepOfCheckout(TestCheckoutFlow):
    @pytest.fixture(scope="function", autouse=True)
    def class_setup(self, browser, setup):
        page = CartPage(browser, browser.current_url)
        page.user_should_be_able_to_fill_first_name_field_of_checkout()
        page.user_should_be_able_to_fill_last_name_field_of_checkout()
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()
        page.should_be_clickable_continue_button_of_checkout()

    def test_user_should_see_second_step_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_second_step_of_checkout()

    def test_user_should_see_correct_quantity_of_selected_items_on_the_second_step_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_item_total_price(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_item_total_price()

    def test_user_should_be_able_to_place_order_on_second_step_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_finish_button_of_checkout()
        page.should_be_success_message_when_order_is_placed()
