from .base_page import BasePage
from .locators import CartPageLocators
from .locators import ProductPageLocators


class CartPage(BasePage):
    def user_should_be_able_to_open_cart_page(self):
        assert self.is_element_present(*CartPageLocators.CART_BUTTON)
        self.go_to_cart()

    def should_be_cart_page(self):
        assert self.is_element_present(*CartPageLocators.CART_TITLE), "Cart page is not opened"

    def should_be_empty_cart(self):
        assert not self.is_element_present(*CartPageLocators.CART_ITEMS), "Cart is not empty"

    def should_be_selected_item_1_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_1), "Cart doesn't contain selected item1"

    def should_be_correct_title_of_item_1_in_cart(self):
        item_1_in_cart = self.browser.find_element(*CartPageLocators.SELECTED_ITEM_1_TITLE)
        item_1 = self.browser.find_element(*ProductPageLocators.ITEM_1)
        assert item_1_in_cart.text == item_1.text, "Name of selected item in cart doesn't match its original name"

    def should_be_selected_item_2_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_2), "Cart doesn't contain selected item2"

    def should_be_correct_title_of_item_2_in_cart(self):
        item_2_in_cart = self.browser.find_element(*CartPageLocators.SELECTED_ITEM_2_TITLE)
        item_2 = self.browser.find_element(*ProductPageLocators.ITEM_2)
        assert item_2_in_cart.text == item_2.text, "Name of selected item in cart doesn't match its original name"

    def should_be_correct_quantity_of_selected_items(self):
        items_quantity = self.browser.find_element(*CartPageLocators.ITEMS_QUANTITY)
        cart_items = self.browser.find_elements(*CartPageLocators.CART_ITEMS)
        assert int(items_quantity.text) == len(cart_items), "Cart shows incorrect items quantity"