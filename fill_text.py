import time
from selenium import webdriver

# from navigate import driver

browser =webdriver.Chrome()
browser.get("https://qxf2.com/selenium-tutorial-main")
if browser.title == "Qxf2 Services: Selenium training main":
    print("Success: Page Load successfully")
else:
    print("Failure:Page Title is incorrect")

#finding the name field using xpath with id
name = browser.find_element("xpath","//input[@id='name']")
#key point : send text to an element using send keys method
name.send_keys('Arjun Bhardwaj')

#find the email field using xpath without id
email = browser.find_element("xpath","//input[@name='email']")
email.send_keys('jhanddu123@gmail.com')

#find the phone no field using id
phone = browser.find_element('id','phone')
phone.send_keys('8000000000')

#sleep is one way to wait things to load
time.sleep(4)
