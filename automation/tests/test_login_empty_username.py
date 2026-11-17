from tests.base_test import BaseTest


class TestLoginEmptyUsername(BaseTest):

    def test_01_empty_username_shows_error(self):
        self.login_page.login("", "secret_sauce")
        assert self.login_page.get_error_message() == "Epic sadface: Username is required"
