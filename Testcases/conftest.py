import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import chrome,ChromeOptions
import time

@pytest.fixture()
def setup(request):
   opt=ChromeOptions()
   opt.add_experimental_option("detach",True)
   request.cls.driver = webdriver.Chrome(options=opt)
   request.cls.driver.get("https://ebilling.rudramtech.in/index.php")
   request.cls.driver.maximize_window()

   yield
   request.cls.driver.close()