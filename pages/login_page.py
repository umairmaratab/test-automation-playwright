from playwright.sync_api import expect
from .base_page import BasePage

class LoginPage(BasePage):
    username = '#user-name'
    password = '#password'
    login_btn = '#login-button'

    def goto_login(self):
        self.goto('')

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
        # wait for inventory page to load
        expect(self.page.locator('.inventory_list')).to_be_visible(timeout=5000)
