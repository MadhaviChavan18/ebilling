from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
     self.driver = driver
    textbox_username_xpath='//input[@id="exampleInputEmail"]'
    textbox_password_xpath='//input[@id="exampleInputPassword"]'
    button_login_xpath='//input[@class="btn btn-primary btn-user btn-block"]'
    text_invalid_xpath="//b[normalize-space()='Please check your username and password.']"
    button_logout_xpath='//ul[@class="navbar-nav ml-auto"]//a[1]'
    msg_box_xpath='//b[normalize-space()="Shop ID"]'

    def input_username(self,username):
         self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
    def input_password(self,passward):
         self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(passward)
    def click_Login(self):
         self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def  invalid_msg(self):
        return self.driver.find_element(By.XPATH,self.text_invalid_xpath).text
    def click_Logout(self):
         self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def  msg_box(self):
        return self.driver.find_element(By.XPATH,self.msg_box_xpath).text