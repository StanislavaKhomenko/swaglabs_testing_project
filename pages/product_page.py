from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_products_grid(self):
        self.is_element_present(*ProductPageLocators.PRODUCTS_GRID)

    def add_product_to_basket_item_1(self):
        self.should_be_add_to_basket_button_item_1()
        self.should_be_remove_button_item_1()

    def add_product_to_basket_item_2(self):
        self.should_be_add_to_basket_button_item_2()
        self.should_be_remove_button_item_2()

    def should_be_add_to_basket_button_item_1(self):
        add_button_item_1 = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ITEM_1_BUTTON)
        add_button_item_1.click()

    def should_be_remove_button_item_1(self):
        assert self.is_element_present(*ProductPageLocators.REMOVE_ITEM_1_BUTTON), "Remove button is not visible for " \
                                                                                   "item 1 "

    def should_be_add_to_basket_button_item_2(self):
        add_button_item_2 = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ITEM_2_BUTTON)
        add_button_item_2.click()

    def should_be_remove_button_item_2(self):
        assert self.is_element_present(*ProductPageLocators.REMOVE_ITEM_2_BUTTON), "Remove button is not visible for " \
                                                                                   "item 2 "
