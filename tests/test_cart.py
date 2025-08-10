from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_to_cart(page):
    login = LoginPage(page)
    login.goto_login()
    login.login('standard_user', 'secret_sauce')
    products = ProductsPage(page)
    products.add_first_to_cart()
    assert products.cart_count() in ('1', '1')  # ensure badge shows 1
    cart = CartPage(page)
    cart.goto_cart()
    assert cart.item_count() == 1
