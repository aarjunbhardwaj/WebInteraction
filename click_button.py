import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")
button = driver.find_element("xpath","//button[text()='Click me!']")
button.click()

time.sleep(3)
driver.close()