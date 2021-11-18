import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import os
import platform

def createChormeDriver():
  if(platform.system() == 'Windows'):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(r".\chromedriver\chromedriver.exe", options=option)
  elif (platform.system() == 'Darwin'):    
    driver = webdriver.Chrome(executable_path='chromedriver')
  return driver