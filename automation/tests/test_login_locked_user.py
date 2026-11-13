from tests.base_test import BaseTest


class TestLoginLockedUser(BaseTest):

    def test_01_locked_out_user_cannot_login(self):
        self.login_page.login("locked_out_user", "secret_sauce")
        assert self.login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."
        assert "inventory" not in self.login_page.page.url
