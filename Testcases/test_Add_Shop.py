import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup")
class Testcase_AddShop:
     def test_add_deatail(self):
         self.driver.find_element(By.XPATH, '//input[@id="exampleInputEmail"]').send_keys(1002)
         self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
         self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
         time.sleep(5)
         self.driver.find_element(By.XPATH, "//input[@placeholder='Shop Name']").send_keys("Om")



