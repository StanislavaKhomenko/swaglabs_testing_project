from selenium.webdriver.common.by import By


class LoginPageLocators():
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    LOGIN_BUTTON = (By.ID, "login-button")
    PASSWORD_FIELD = (By.ID, "password")
    PRODUCTS_GRID = (By.ID, "inventory_container")
    USERNAME_FIELD = (By.ID, "user-name")


class ProductPageLocators():
    ADD_TO_CART_ITEM_1_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_TO_CART_ITEM_2_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    FIRST_ITEM_AFTER_SORTING_ADD_TO_CART = (By.CSS_SELECTOR, ".inventory_item:nth-child(1):first-of-type button")
    FIRST_ITEM_AFTER_SORTING_TITLE = (By.CSS_SELECTOR, ".inventory_item:nth-child(1):first-of-type a > "
                                                       ".inventory_item_name")
    FIRST_ITEM_AFTER_SORTING_PRICE = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) > .inventory_item_description > "
                                                       ".pricebar > .inventory_item_price")
    ITEM_1 = (By.ID, "item_2_title_link")
    ITEM_2 = (By.ID, "item_0_title_link")
    PRODUCTS_GRID = (By.ID, "inventory_container")
    PRODUCTS_SORTING = (By.CLASS_NAME, "product_sort_container")
    REMOVE_ITEM_1_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_ITEM_2_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    SORT_BY_PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, "option[value='lohi']")
    SORT_BY_PRICE_HIGH_TO_LOW = (By.CSS_SELECTOR, "option[value='hilo']")
    SORT_BY_NAME_FROM_A_TO_Z = (By.CSS_SELECTOR, "option[value='az']")
    SORT_BY_NAME_FROM_Z_TO_A = (By.CSS_SELECTOR, "option[value='za']")
    SORTED_BY_NAME_ITEMS_ARRAY = (By.CLASS_NAME, "inventory_item_name")
    SORTED_BY_PRICE_ITEMS_ARRAY = (By.CLASS_NAME, "inventory_item_price")


class CartPageLocators():
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_list > .cart_item")
    CART_TITLE = (By.CLASS_NAME, "title")
    CANCEL_BUTTON = (By.ID, "cancel")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CHECKOUT_COMPLETE_TITLE = (By.CLASS_NAME, "complete-header")
    CHECKOUT_FIRST_NAME_FIELD = (By.ID, "first-name")
    CHECKOUT_FIRST_NAME_VALUE = (By.CSS_SELECTOR, "#first-name[value='John']")
    CHECKOUT_LAST_NAME_FIELD = (By.ID, "last-name")
    CHECKOUT_LAST_NAME_VALUE = (By.CSS_SELECTOR, "#last-name[value='Doe']")
    CHECKOUT_POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CHECKOUT_POSTAL_CODE_VALUE = (By.CSS_SELECTOR, "#postal-code[value='03148']")
    CHECKOUT_SUMMARY = (By.CLASS_NAME, "summary_info")
    CHECKOUT_SUMMARY_PRICE = (By.CLASS_NAME, "summary_subtotal_label")
    CONTINUE_BUTTON = (By.ID, "continue")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    ERROR_MESSAGE_CHECKOUT = (By.CSS_SELECTOR, "[data-test='error']")
    FINISH_BUTTON = (By.ID, "finish")
    ITEMS_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEMS_QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_ITEM_1_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_ITEM_2_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    SELECTED_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    SELECTED_ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    SELECTED_ITEM_1_TITLE = (By.ID, "item_2_title_link")
    SELECTED_ITEM_2_TITLE = (By.ID, "item_0_title_link")
