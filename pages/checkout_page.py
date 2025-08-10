from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST = '#first-name'
    LAST = '#last-name'
    ZIP = '#postal-code'
    CONTINUE = '#continue'
    FINISH = '#finish'
    COMPLETE_TEXT = '.complete-header'

    def fill_info(self, first, last, zipc):
        self.page.fill(self.FIRST, first)
        self.page.fill(self.LAST, last)
        self.page.fill(self.ZIP, zipc)
        self.page.click(self.CONTINUE)

    def finish(self):
        self.page.click(self.FINISH)

    def is_complete(self):
        return self.page.locator(self.COMPLETE_TEXT).inner_text().strip()
