## Following test is or testin g title and enquiry no. in Credence ewbside
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium import webdriver

class Test_003:
    def test_credence(self):
        driver = webdriver.Firefox()
        driver.get("https://credence.in/")
        offers = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)
        if driver.title == 'Credence':
            assert True
        else:
            assert False

    def test_credence_(self):
        driver = webdriver.Firefox()
        driver.get("https://credence.in/")
        time.sleep(2) #it's required for open next web element
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        le = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a").copy())

        print(le)

        for r in range(1, le+1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            list = []
            list.append(contact)
            # print(list)
            if "+91 9091929355" in list:
                print(list)
                break
                # print(list)
            assert True
        else:
            assert False