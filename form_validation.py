import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")
button =driver.find_element('xpath',"//button[text()='Click me!']")
button.click()
#Pause the script to wait for validation messages to load
time.sleep(3)

# if the validation message for name field
try:
    driver.find_element("xpath","//label[text()='Please enter your name']")
except Exception as e:
    result_flag = False
else:
    result_flag = True
    if result_flag is True:
        print("Validation message for enter your name")
    else:
        print("Not message showing for enter your name")
        
driver.close()