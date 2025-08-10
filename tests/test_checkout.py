from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(page):
    login = LoginPage(page)
    login.goto_login()
    login.login('standard_user', 'secret_sauce')
    products = ProductsPage(page)
    products.add_first_to_cart()
    cart = CartPage(page)
    cart.goto_cart()
    cart.checkout()
    checkout = CheckoutPage(page)
    checkout.fill_info('John','Doe','12345')
    checkout.finish()
    assert 'THANK YOU FOR YOUR ORDER' in checkout.is_complete().upper()
