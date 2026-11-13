from tests.base_test import BaseTest


class TestProducts(BaseTest):

    def test_login(self):
        self.login_page.login("standard_user","secret_sauce")

    def test_logout(self):
        self.products_page.add_to_cart("Sauce Labs Fleece Jacket")
        self.products_page.open_cart()
        self.your_cart_page.checkout()
        self.your_information_page.logout()








