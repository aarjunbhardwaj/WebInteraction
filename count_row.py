import time
from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://qxf2.com/selenium-tutorial-main")

#finding the element in the table
table = driver.find_element("xpath","//table[@name='Example Table']")

#finding rows in table
rows = table.find_elements("xpath","//tbody/descendant::tr")
print(f"Total no. of rows: {len(rows)}")

time.sleep(3)
driver.close()