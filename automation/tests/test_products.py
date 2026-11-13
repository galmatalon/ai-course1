from tests.base_test import BaseTest


class TestProducts(BaseTest):

    def test_login(self):
        self.login_page.login("standard_user","secret_sauce")

    def test_add_product(self):
        self.products_page.sort("lohi")
        self.products_page.add_to_cart("Sauce Labs Fleece Jacket")
        self.products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        self.products_page.open_cart()
        self.your_cart_page.checkout()
        self.your_information_page.fill_info("Gal", "", "")
        self.your_information_page.fill_info("Gal", "Hello", "888")








