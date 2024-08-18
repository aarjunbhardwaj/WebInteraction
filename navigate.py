from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://qxf2.com/selenium-tutorial-main')
if driver.title == "Qxf2 Services: Selenium training main":
    print("Success: Page load successfully")
else:
    print("Page Title is incorrect")