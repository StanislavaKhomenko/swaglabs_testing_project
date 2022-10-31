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
