from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = '.cart_item'
    CHECKOUT_BTN = '#checkout'

    def goto_cart(self):
        self.page.click('.shopping_cart_link')

    def item_count(self):
        return self.page.locator(self.CART_ITEM).count()

    def checkout(self):
        self.page.click(self.CHECKOUT_BTN)
