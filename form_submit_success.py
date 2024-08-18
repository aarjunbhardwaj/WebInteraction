import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")

#find the name field and fill the name
name = driver.find_element("xpath","//input[@id='name']")
name.send_keys("Arjun Bhardwaj")

#find the email field and fill the name
email = driver.find_element("xpath","//input[@name='email']")
email.send_keys("jhanddu1533@gmail.com")

#find the number field and fill the phone number
phone = driver.find_element("id","phone")
phone.send_keys("9000000000")

#identify the xpath for click me button and clicking on it

button = driver.find_element("xpath","//button[text()='Click me!']")
button.click()

#waiting for new page to load
time.sleep(3)

#varify to user taken to an tutorial page redirected [url]
if driver.current_url=="https://qxf2.com/selenium-tutorial-redirect":
    print("Success")
else:
    print("failure")

#closing the browser
driver.close()
