from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
import pytest

link = "https://www.saucedemo.com/inventory.html"


class TestProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.user_should_be_able_to_login()
        page.should_be_authorized_user()

    def test_user_can_see_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_products_grid()

    def test_user_can_open_cart_and_see_it_empty(self, browser):
        page = CartPage(browser, link)
        page.open()
        page.go_to_cart()
        page.should_be_cart_page()
        page.should_be_empty_cart()

    class TestUserCanSortProducts():
        def test_user_can_see_sorting_option(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_sorting_option()

        def test_user_can_click_on_sort_button_and_see_sorting_options(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_clickable_sorting_option()
            page.should_be_all_sorting_options()

        def test_user_can_sort_products_from_low_to_high(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_correct_sorting_by_price_from_low_to_high()

        def test_user_can_sort_products_from_high_to_low(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_correct_sorting_by_price_from_high_to_low()

        def test_user_can_sort_products_from_a_to_z(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_correct_sorting_by_name_from_a_to_z()

        def test_user_can_sort_products_from_z_to_a(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_correct_sorting_by_name_from_z_to_a()

    class TestUserCanAddProduct1ToCart():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_add_to_basket_button_item_1()

        def test_user_should_see_remove_button_after_adding_product_1_to_basket(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_remove_button_item_1()

        def test_user_should_be_able_to_open_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_cart_page()

        def test_user_can_see_correct_quantity_of_selected_items(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_correct_quantity_of_selected_items()

        def test_user_should_see_selected_item_in_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_selected_item_1_in_cart()

        def test_can_see_correct_title_of_selected_item(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_correct_title_of_item_1_in_cart()

        def test_user_can_go_back_to_products_from_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_able_to_go_back_to_products()

    class TestUserCanAddProduct2ToCart():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_add_to_basket_button_item_1()
            page.should_be_add_to_basket_button_item_2()

        def test_user_should_see_remove_button_after_adding_product_2_to_basket(self, browser):
            page = ProductPage(browser, link)
            page.open()
            page.should_be_remove_button_item_2()

        def test_user_should_be_able_to_open_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_cart_page()

        def test_user_can_see_correct_quantity_of_selected_items(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_correct_quantity_of_selected_items()

        def test_user_should_see_both_items_in_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_selected_item_1_in_cart()
            page.should_be_selected_item_2_in_cart()

        def test_can_see_correct_title_of_selected_item(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_correct_title_of_item_2_in_cart()

        def test_user_can_go_back_to_products_from_cart(self, browser):
            page = CartPage(browser, link)
            page.open()
            page.go_to_cart()
            page.should_be_able_to_go_back_to_products()
