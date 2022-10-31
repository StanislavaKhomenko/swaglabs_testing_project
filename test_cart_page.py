from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

link = "https://www.saucedemo.com/cart.html"


class TestCartPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_should_be_able_to_login()
        page.should_be_authorized_user()


class TestUserShouldSeeCartPageAndNoItemsInItAfterLogging(TestCartPage):
    def test_user_can_see_cart_page(self, browser, setup):
        page = CartPage(browser, link)
        page.open()
        page.should_be_cart_page()

    def test_user_can_see_cart_empty_if_no_items_were_selected(self, browser, setup):
        page = CartPage(browser, link)
        page.open()
        page.should_be_cart_page()
        page.should_be_empty_cart()


class TestUserShouldSeeCorrectInformationOnItem1InCart(TestCartPage):
    @pytest.fixture(scope="function", autouse=True)
    def class_setup(self, browser, setup):
        product_link = "https://www.saucedemo.com/inventory.html"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart_item_1()
        page.go_to_cart()

    def test_user_should_see_correct_items_quantity_in_cart_after_adding_item_1(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_selected_item_1_in_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_selected_item_1_in_cart()

    def test_user_should_see_correct_title_of_item_1_in_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_cart_page()
        page.should_be_correct_title_of_item_1_in_cart()

    def test_user_can_go_back_to_products_after_adding_item_1_to_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_able_to_go_back_to_products()
        page = ProductPage(browser, browser.current_url)
        page.should_be_products_grid()


class TestUserShouldSeeCorrectInformationOnItem2InCart(TestCartPage):
    @pytest.fixture(scope="function", autouse=True)
    def class_setup(self, browser, setup):
        product_link = "https://www.saucedemo.com/inventory.html"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart_item_1()
        page.add_product_to_cart_item_2()
        page.go_to_cart()

    def test_user_should_see_correct_items_quantity_in_cart_after_adding_2_items(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_cart_page()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_both_items_in_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_selected_item_1_in_cart()
        page.should_be_selected_item_2_in_cart()

    def test_user_should_see_correct_title_of_item_2_in_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_title_of_item_2_in_cart()

    def test_user_can_go_back_to_products_after_adding_both_items_to_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_able_to_go_back_to_products()
        page = ProductPage(browser, browser.current_url)
        page.should_be_products_grid()


class TestUserShouldBeAbleToRemoveItemFromCart(TestCartPage):
    @pytest.fixture(scope="function", autouse=True)
    def class_setup(self, browser, setup):
        product_link = "https://www.saucedemo.com/inventory.html"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart_item_1()
        page.add_product_to_cart_item_2()
        page.go_to_cart()

    def test_user_should_see_remove_buttons(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_remove_item_1_button()
        page.should_be_remove_item_2_button()

    def test_user_can_click_on_remove_item_2_button(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_remove_item_2_button()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_be_able_to_continue_shopping_and_see_removed_item_available_for_adding(self, browser):
        TestUserShouldBeAbleToRemoveItemFromCart.test_user_can_click_on_remove_item_2_button(self, browser)
        page = CartPage(browser, browser.current_url)
        page.should_be_able_to_go_back_to_products()
        page = ProductPage(browser, browser.current_url)
        page.should_be_products_grid()
        page.should_be_add_to_cart_button_item_2()


class TestUserShouldCheckout(TestCartPage):
    @pytest.fixture(scope="function", autouse=True)
    def class_setup(self, browser, setup):
        product_link = "https://www.saucedemo.com/inventory.html"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart_item_2()
        page.should_be_sorting_by_price_from_low_to_high_and_adding_first_option_to_cart()
        page.should_be_first_item_of_sorted_list_in_cart()
        page.go_to_cart()

    def test_user_should_see_checkout_button_and_be_able_to_click_on_it(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_checkout_button()
        page.should_be_clickable_checkout_button()

    def test_user_should_see_first_step_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.should_be_first_step_of_checkout()

    def test_user_should_see_cancel_button_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.should_be_cancel_button_of_checkout()

    def test_user_should_be_able_to_left_checkout_and_see_selected_items_in_cart(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.should_be_clickable_cancel_button_of_checkout()
        page.should_be_correct_quantity_of_selected_items()
        page.should_be_selected_item_2_in_cart()

    def test_user_should_be_able_to_fill_first_name_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_first_name_field_of_checkout()

    def test_user_should_see_correct_value_of_first_name_field_of_checkout_after_filling_it(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_first_name_field_of_checkout()
        page.should_be_correct_value_of_first_name_field_of_checkout()

    def test_user_should_be_able_to_fill_last_name_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_last_name_field_of_checkout()

    def test_user_should_see_correct_value_of_last_name_field_of_checkout_after_filling_it(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_last_name_field_of_checkout()
        page.should_be_correct_value_of_last_name_field_of_checkout()

    def test_user_should_be_able_to_fill_postal_code_field_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()

    def test_user_should_see_correct_value_of_postal_code_field_of_checkout_after_filling_it(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()
        page.should_be_correct_value_of_postal_code_field_of_checkout()

    def test_user_should_see_continue_button_on_the_first_step_of_checkout(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.should_be_continue_button_of_checkout()

    def test_user_should_see_error_message_by_clicking_on_continue_button_with_no_data_entered(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.should_be_clickable_continue_button_of_checkout()
        page.should_be_error_message_when_user_tries_to_pass_first_step_of_checkout_without_data()

    def test_user_should_fill_fields_of_first_step_of_checkout_and_go_on(self, browser):
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_checkout_button()
        page.user_should_be_able_to_fill_first_name_field_of_checkout()
        page.user_should_be_able_to_fill_last_name_field_of_checkout()
        page.user_should_be_able_to_fill_postal_code_field_of_checkout()
        page.should_be_clickable_continue_button_of_checkout()

    def test_user_should_see_second_step_of_checkout(self, browser):
        TestUserShouldCheckout.test_user_should_fill_fields_of_first_step_of_checkout_and_go_on(self, browser)
        page = CartPage(browser, browser.current_url)
        page.should_be_second_step_of_checkout()

    def test_user_should_see_correct_quantity_of_selected_items_on_the_second_step_of_checkout(self, browser):
        TestUserShouldCheckout.test_user_should_fill_fields_of_first_step_of_checkout_and_go_on(self, browser)
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_item_total_price(self, browser):
        TestUserShouldCheckout.test_user_should_fill_fields_of_first_step_of_checkout_and_go_on(self, browser)
        page = CartPage(browser, browser.current_url)
        page.should_be_correct_item_total_price()

    def test_user_should_be_able_to_place_order_on_second_step_of_checkout(self, browser):
        TestUserShouldCheckout.test_user_should_fill_fields_of_first_step_of_checkout_and_go_on(self, browser)
        page = CartPage(browser, browser.current_url)
        page.should_be_clickable_finish_button_of_checkout()
        page.should_be_success_message_when_order_is_placed()
