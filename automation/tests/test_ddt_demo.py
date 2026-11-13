import pytest

from tests.base_test import BaseTest


class TestDemo(BaseTest):

    @pytest.mark.parametrize("x, y, total", [(2,3,5), (5,3,8)])
    def test_calc_2_numbers(self, x, y, total):
        assert x + y == total




