import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://qxf2.com/selenium-tutorial-main")
#identify the dropdown and clicking on it
dropdown_element = driver.find_element("xpath", "//button[@data-toggle='dropdown']")
dropdown_element.click()
time.sleep(2)
#Lacating a particular option and clicking on it
driver.find_element("xpath","//a[text()='Male']").click()
time.sleep(4)