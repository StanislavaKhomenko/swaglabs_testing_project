from selenium.webdriver.common.by import By


class LoginPageLocators():
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_GRID = (By.ID, "inventory_container")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")


class ProductPageLocators():
    PRODUCTS_GRID = (By.ID, "inventory_container")
    ITEM_1 = (By.ID, "item_2_title_link")
    ADD_TO_CART_ITEM_1_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    REMOVE_ITEM_1_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    ITEM_2 = (By.ID, "item_0_title_link")
    ADD_TO_CART_ITEM_2_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_ITEM_2_BUTTON = (By.ID, "remove-sauce-labs-bike-light")


class CartPageLocators():
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_TITLE = (By.CLASS_NAME, "title")
    SELECTED_ITEM_1_TITLE = (By.ID, "item_2_title_link")
    SELECTED_ITEM_2_TITLE = (By.ID, "item_0_title_link")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_list > .cart_item")
    ITEMS_QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")
