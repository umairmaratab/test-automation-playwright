class BasePage:
    def __init__(self, page, base_url='https://www.saucedemo.com/'):
        self.page = page
        self.base_url = base_url

    def goto(self, path=''):
        url = self.base_url.rstrip('/') + '/' + path.lstrip('/')
        self.page.goto(url)

    def text(self, selector):
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()
