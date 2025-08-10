from .base_page import BasePage

class ProductsPage(BasePage):
    FIRST_ADD_BUTTON = '.inventory_item button.btn_inventory'
    CART_BADGE = '.shopping_cart_badge'
    SORT_SELECT = '.product_sort_container'
    FIRST_PRODUCT_NAME = '.inventory_item_name'

    def add_first_to_cart(self):
        self.page.click(self.FIRST_ADD_BUTTON)

    def cart_count(self):
        locator = self.page.locator(self.CART_BADGE)
        return locator.inner_text() if locator.count() else '0'

    def filter_products(self, option_text):
        # select by visible text
        select = self.page.locator(self.SORT_SELECT)
        select.select_option(label=option_text)

    def first_product_name(self):
        return self.page.locator(self.FIRST_PRODUCT_NAME).nth(0).inner_text()
