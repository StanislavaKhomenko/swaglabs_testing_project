from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest

link = "https://www.saucedemo.com/inventory.html"


class TestProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_should_be_able_to_login()
        page.should_be_authorized_user()


class TestUserShouldSeeProductPageAndEmptyCartAfterLogging(TestProductPage):
    def test_user_can_see_product_page(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_products_grid()

    def test_user_can_open_cart_and_see_it_empty(self, browser, setup):
        page = CartPage(browser, link)
        page.open()
        page.go_to_cart()
        page.should_be_cart_page()
        page.should_be_empty_cart()


class TestUserCanSortProducts(TestProductPage):
    def test_user_can_see_sorting_option(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_option()

    def test_user_can_click_on_sort_button_and_see_sorting_options(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_clickable_sorting_option()
        page.should_be_all_sorting_options()

    def test_user_can_sort_products_from_low_to_high(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_sorting_by_price_from_low_to_high()

    def test_user_can_sort_products_from_high_to_low(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_sorting_by_price_from_high_to_low()

    def test_user_can_sort_products_from_a_to_z(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_sorting_by_name_from_a_to_z()

    def test_user_can_sort_products_from_z_to_a(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_sorting_by_name_from_z_to_a()


class TestUserCanSelectProductsFromSortedList(TestProductPage):
    def test_user_can_sort_products_by_price_and_select_first_option_low(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_price_from_low_to_high_and_adding_first_option_to_cart()
        page = CartPage(browser, link)
        page.go_to_cart()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_product_selected_from_list_sorted_by_price_low(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_price_from_low_to_high_and_adding_first_option_to_cart()
        page.should_be_first_item_of_sorted_list_in_cart()

    def test_user_can_sort_products_by_price_and_select_first_option_high(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_price_from_high_to_low_and_adding_first_option_to_cart()
        page = CartPage(browser, link)
        page.go_to_cart()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_product_selected_from_list_sorted_by_price_high(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_price_from_high_to_low_and_adding_first_option_to_cart()
        page.should_be_first_item_of_sorted_list_in_cart()

    def test_user_can_sort_products_by_name_and_select_first_option_from_a(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_name_from_a_to_z_and_adding_first_option_to_cart()
        page = CartPage(browser, link)
        page.go_to_cart()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_product_selected_from_list_sorted_by_name_a(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_name_from_a_to_z_and_adding_first_option_to_cart()
        page.should_be_first_item_of_sorted_list_in_cart()

    def test_user_can_sort_products_by_name_and_select_first_option_from_z(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_name_from_z_to_a_and_adding_first_option_to_cart()
        page = CartPage(browser, link)
        page.go_to_cart()
        page.should_be_correct_quantity_of_selected_items()

    def test_user_should_see_correct_product_selected_from_list_sorted_by_name_z(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_sorting_by_name_from_z_to_a_and_adding_first_option_to_cart()
        page.should_be_first_item_of_sorted_list_in_cart()


class TestUserCanAddProduct1ToCart(TestProductPage):
    def test_user_can_add_product_1_to_cart(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button_item_1()
        page.should_be_clickable_add_to_cart_button_item_1()

    def test_user_should_see_remove_button_after_adding_product_1_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_remove_button_item_1()


class TestUserCanAddProduct2ToCart(TestProductPage):
    def test_user_can_add_product_2_to_cart(self, browser, setup):
        page = ProductPage(browser, link)
        page.should_be_add_to_cart_button_item_1()
        page.should_be_clickable_add_to_cart_button_item_1()
        page.should_be_add_to_cart_button_item_2()
        page.should_be_clickable_add_to_cart_button_item_2()

    def test_user_should_see_remove_button_after_adding_product_2_to_basket(self, browser, setup):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_remove_button_item_2()
