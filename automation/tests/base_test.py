from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.your_cart_page import YourCartPage
from pages.your_information_page import YourInformationPage


class BaseTest:

    login_page: LoginPage
    products_page: ProductsPage
    your_cart_page: YourCartPage
    your_information_page: YourInformationPage


