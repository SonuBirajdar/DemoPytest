import pytest


class Test_002:
    # @pytest.mark.group1
    def test_sum_004(self):
        a = 3
        b = 5
        sum = a+b
        if sum == 8:
            assert True
        else:
            assert False