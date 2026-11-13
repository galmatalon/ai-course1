from tests.base_test import BaseTest


class TestProducts(BaseTest):

    def test_01_login_failed(self):
        self.login_page.login("standard_user1","secret_sauce")
        print(self.login_page.get_error_message())

    def test_02_login_failed(self):
        self.login_page.login("standard_user","secret_sauce1")

    def test_03_login_failed(self):
        self.login_page.login("standard_user1","secret_sauce1")

    def test_04_login_failed(self):
        self.login_page.login("standard_user","")







