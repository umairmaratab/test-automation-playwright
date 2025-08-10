from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login(page):
    login = LoginPage(page)
    login.goto_login()
    login.login('standard_user', 'secret_sauce')
    products = ProductsPage(page)
    assert products.first_product_name()  # non-empty
