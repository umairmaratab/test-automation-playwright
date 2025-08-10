from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_filter_low_to_high(page):
    login = LoginPage(page)
    login.goto_login()
    login.login('standard_user', 'secret_sauce')
    products = ProductsPage(page)
    products.filter_products('Price (low to high)')
    first_name = products.first_product_name().lower()
    assert first_name  # basic check that we have a product
