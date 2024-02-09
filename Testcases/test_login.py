import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time
from PageObject.LoginPage import Login
from Utilities.logger import Logclass

@pytest.mark.usefixtures("setup")
class Testcase_Login(Logclass):
    def test_Valid_Login(self):
        log = self.getclass()
        lg = Login(self.driver)
        log.info("Testcase_login")
        log.info("Testcases started")
        lg.input_username("1002")
        log.info("Entered username")
        lg.input_password("Bright@123")
        log.info("Entered Password")
        lg.click_Login()
        log.info("click login")
        # time.sleep(10)
        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys(1002)
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()

        if 'Shop Id' in lg.msg_box():
            assert  True
            log.info("Test case pass")
        else:
            self.driver.save_screenshot('screenshot\\test_Valid_Login.png')
            log.critical("Test case fail")
    def test_InValid_Login_withoutid(self):
        lg = Login(self.driver)
        lg.input_username("")
        lg.input_password("Bright@123")
        lg.click_Login()

        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        # time.sleep(5)

        expected_result = 'Please check your username and password.'
        #actual_result =self.driver.find_element(By.XPATH, "//b[normalize-space()='Please check your username and password.']").text
        assert lg.invalid_msg().__eq__(expected_result)




    def test_InValid_Login_withoutPassword(self):
        time.sleep(10)
        lg=Login(self.driver)
        lg.input_username("1002")
        lg.input_password("")
        lg.click_Login()
        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys("1002")
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        # time.sleep(5)
        expected_result = 'Please check your username and password.'
        assert lg.invalid_msg().__eq__(expected_result)


    def test_InValid_Login_withNull(self):
        time.sleep(10)
        lg=Login(self.driver)
        lg.input_username("")
        lg.input_password("")
        lg.click_Login()
        # self.driver.find_element(By.XPATH,'//input[@id="exampleInputEmail"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys()
        # self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
        # time.sleep(5)
        expected_result = 'Please check your username and password.'
        assert lg.invalid_msg().__eq__(expected_result)


    def test_Logout(self):
           time.sleep(10)
           lg=Login(self.driver)
           lg.input_username("1002")
           lg.input_password("Bright@123")
           lg.click_Login()
           lg.click_Logout()
           # self. driver.find_element(By.XPATH, '//input[@id="exampleInputEmail"]').send_keys(1002)
           # self. driver.find_element(By.XPATH, '//input[@id="exampleInputPassword"]').send_keys("Bright@123")
           # self. driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-user btn-block"]').click()
           # time.sleep(5)
           # self.driver.find_element(By.XPATH,'//ul[@class="navbar-nav ml-auto"]//a[1]').click()


