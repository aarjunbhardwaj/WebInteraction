import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")

#Locating the checkbox and clicking on it
checkbox = driver.find_element('xpath',"//input[@type='checkbox']")
checkbox.click()

time.sleep(3)
driver.close()