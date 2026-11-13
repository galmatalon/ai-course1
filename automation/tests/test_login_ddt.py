import pytest

from tests.base_test import BaseTest


class TestProducts(BaseTest):

    __DATA = [("standard_user1","secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
            ("standard_user","secret_sauce1", "Epic sadface: Username and password do not match any user in this service"),
            ("standard_user1","secret_sauce1", "Epic sadface: Username and password do not match any user in this service"),
            ("standard_user","", "Password is required")]

    @pytest.mark.parametrize("user, password, error_msg", __DATA)
    def test_01_login_failed(self, user, password, error_msg):
        self.login_page.login(user,password)
        assert self.login_page.get_error_message() == error_msg









