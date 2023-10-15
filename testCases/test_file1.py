import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium import webdriver


class Test_Py:
    # @pytest.mark.xfail
    def test_sum_001(self):
        a = 3
        b = 5
        sum = a+b
        if sum == 8:
            assert True
        else:
            assert False

    # @pytest.mark.skip
    def test_mul_002(self):
        a = 3
        b = 5
        mul = a*b
        if mul == 16:
            assert True
        else:
            assert False

    def mul_002(self):##it will not considered as testcase
        a = 3
        b = 5
        mul = a*b
        if mul == 16:
            assert True
        else:
            assert False

###below tesecase is for google logo
    # @pytest.mark.group1
    def test_google(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.XPATH, "//img[@class='lnXdpd']").is_displayed()
        print(logo)
        if logo == True:
            assert True
        else:
            assert False


