from .base_page import BasePage
from .locators import CartPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_products_grid(self):
        self.is_element_present(*ProductPageLocators.PRODUCTS_GRID)

    def add_product_to_cart_item_1(self):
        self.should_be_add_to_cart_button_item_1()
        self.should_be_clickable_add_to_cart_button_item_1()
        self.should_be_remove_button_item_1()

    def add_product_to_cart_item_2(self):
        self.should_be_add_to_cart_button_item_2()
        self.should_be_clickable_add_to_cart_button_item_2()
        self.should_be_remove_button_item_2()

    def should_be_add_to_cart_button_item_1(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_ITEM_1_BUTTON), "Add to cart button of Item 1 " \
                                                                                        "is absent"

    def should_be_clickable_add_to_cart_button_item_1(self):
        add_button_item_1 = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ITEM_1_BUTTON)
        add_button_item_1.click()

    def should_be_remove_button_item_1(self):
        assert self.is_element_present(*ProductPageLocators.REMOVE_ITEM_1_BUTTON), "Remove button is not visible for " \
                                                                                   "item 1 "

    def should_be_add_to_cart_button_item_2(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_ITEM_1_BUTTON), "Add to cart button of Item 2 " \
                                                                                        "is absent"

    def should_be_clickable_add_to_cart_button_item_2(self):
        add_button_item_2 = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ITEM_2_BUTTON)
        add_button_item_2.click()

    def should_be_remove_button_item_2(self):
        assert self.is_element_present(*ProductPageLocators.REMOVE_ITEM_2_BUTTON), "Remove button is not visible for " \
                                                                                   "item 2 "

    def should_be_sorting_option(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCTS_SORTING), "Products sorting option is absent"

    def should_be_clickable_sorting_option(self):
        products_sorting_button = self.browser.find_element(*ProductPageLocators.PRODUCTS_SORTING)
        products_sorting_button.click()

    def should_be_all_sorting_options(self):
        self.should_be_sorting_by_price_from_low_to_high()
        self.should_be_sorting_by_price_from_high_to_low()
        self.should_be_sorting_by_name_from_a_to_z()
        self.should_be_sorting_by_name_from_z_to_a()

    def should_be_sorting_by_price_from_low_to_high(self):
        assert self.is_element_present(*ProductPageLocators.SORT_BY_PRICE_LOW_TO_HIGH)

    def should_be_sorting_by_price_from_high_to_low(self):
        assert self.is_element_present(*ProductPageLocators.SORT_BY_PRICE_HIGH_TO_LOW)

    def should_be_sorting_by_name_from_a_to_z(self):
        assert self.is_element_present(*ProductPageLocators.SORT_BY_NAME_FROM_A_TO_Z)

    def should_be_sorting_by_name_from_z_to_a(self):
        assert self.is_element_present(*ProductPageLocators.SORT_BY_NAME_FROM_Z_TO_A)

    def should_be_correct_sorting_by_price_from_low_to_high(self):
        self.should_be_clickable_sorting_option()
        sort_by_price_from_low_to_high = self.browser.find_element(*ProductPageLocators.SORT_BY_PRICE_LOW_TO_HIGH)
        sort_by_price_from_low_to_high.click()
        sorted_items_array = self.browser.find_elements(*ProductPageLocators.SORTED_BY_PRICE_ITEMS_ARRAY)
        sorted_list = []

        for i in sorted_items_array:
            sorted_list.append(float(i.text[1:]))

        assert sorted_list == sorted(sorted_list), "Sorting by price from low to high hasn't been done accurate"

    def should_be_correct_sorting_by_price_from_high_to_low(self):
        self.should_be_clickable_sorting_option()
        sort_by_price_from_high_to_low = self.browser.find_element(*ProductPageLocators.SORT_BY_PRICE_HIGH_TO_LOW)
        sort_by_price_from_high_to_low.click()
        sorted_items_array = self.browser.find_elements(*ProductPageLocators.SORTED_BY_PRICE_ITEMS_ARRAY)
        sorted_list = []

        for i in sorted_items_array:
            sorted_list.append(float(i.text[1:]))

        assert sorted_list == sorted(sorted_list, reverse=True), "Sorting by price from high to low hasn't been done" \
                                                                 "accurate"

    def should_be_correct_sorting_by_name_from_a_to_z(self):
        self.should_be_clickable_sorting_option()
        sort_by_name_from_a_to_z = self.browser.find_element(*ProductPageLocators.SORT_BY_NAME_FROM_A_TO_Z)
        sort_by_name_from_a_to_z.click()
        sorted_items_array = self.browser.find_elements(*ProductPageLocators.SORTED_BY_NAME_ITEMS_ARRAY)
        sorted_list = []

        for i in sorted_items_array:
            sorted_list.append(i.text)

        assert sorted_list == sorted(sorted_list), "Sorting by name from A to Z hasn't been done accurate"

    def should_be_correct_sorting_by_name_from_z_to_a(self):
        self.should_be_clickable_sorting_option()
        sort_by_name_from_z_to_a = self.browser.find_element(*ProductPageLocators.SORT_BY_NAME_FROM_Z_TO_A)
        sort_by_name_from_z_to_a.click()
        sorted_items_array = self.browser.find_elements(*ProductPageLocators.SORTED_BY_NAME_ITEMS_ARRAY)
        sorted_list = []

        for i in sorted_items_array:
            sorted_list.append(i.text)

        assert sorted_list == sorted(sorted_list, reverse=True), "Sorting by name from Z to A hasn't been done accurate"

    def add_first_item_of_sorted_list_to_cart(self):
        first_item_of_sorted_list = self.browser.find_element(*ProductPageLocators.FIRST_ITEM_AFTER_SORTING_ADD_TO_CART)
        first_item_of_sorted_list.click()

    def should_be_sorting_by_price_from_low_to_high_and_adding_first_option_to_cart(self):
        self.should_be_sorting_by_price_from_low_to_high()
        self.should_be_correct_sorting_by_price_from_low_to_high()
        self.add_first_item_of_sorted_list_to_cart()

    def should_be_sorting_by_price_from_high_to_low_and_adding_first_option_to_cart(self):
        self.should_be_sorting_by_price_from_high_to_low()
        self.should_be_correct_sorting_by_price_from_high_to_low()
        self.add_first_item_of_sorted_list_to_cart()

    def should_be_sorting_by_name_from_a_to_z_and_adding_first_option_to_cart(self):
        self.should_be_sorting_by_name_from_a_to_z()
        self.should_be_correct_sorting_by_name_from_a_to_z()
        self.add_first_item_of_sorted_list_to_cart()

    def should_be_sorting_by_name_from_z_to_a_and_adding_first_option_to_cart(self):
        self.should_be_sorting_by_name_from_z_to_a()
        self.should_be_correct_sorting_by_name_from_z_to_a()
        self.add_first_item_of_sorted_list_to_cart()

    def should_be_correct_price_of_first_item_of_sorted_list_in_cart(self):
        first_item_of_sorted_list_price = self.browser.find_element(*ProductPageLocators.FIRST_ITEM_AFTER_SORTING_PRICE)
        price_of_selected_item_in_cart = self.browser.find_element(*CartPageLocators.SELECTED_ITEM_PRICE)
        assert first_item_of_sorted_list_price.text == price_of_selected_item_in_cart.text, "Price of selected item " \
                                                                                            "in cart doesn't match " \
                                                                                            "it's original price "

    def should_be_correct_title_of_first_item_of_sorted_list_in_cart(self):
        first_item_of_sorted_list_title = self.browser.find_element(*ProductPageLocators.FIRST_ITEM_AFTER_SORTING_TITLE)
        title_of_selected_item_in_cart = self.browser.find_element(*CartPageLocators.SELECTED_ITEM_TITLE)
        assert first_item_of_sorted_list_title.text == title_of_selected_item_in_cart.text, "Title of selected item " \
                                                                                            "in cart doesn't match " \
                                                                                            "it's original title "

    def should_be_first_item_of_sorted_list_in_cart(self):
        self.should_be_correct_price_of_first_item_of_sorted_list_in_cart()
        self.should_be_correct_title_of_first_item_of_sorted_list_in_cart()
