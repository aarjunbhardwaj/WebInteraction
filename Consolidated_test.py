import time
from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()

#navigation
driver.get("http://qxf2.com/selenium-tutorial-main")

#Finding the Example table element in the page
table = driver.find_element("xpath","//table[@name='Example Table']")

# Finding no of rows in the table by getting the tr elements in the table
rows = table.find_elements("xpath","//tbody/descendant::tr")

#creating list to store data
result_data = []

for i in range(0,len(rows)):
    cols = rows[i].find_elements("tag name","td")
    cols_data = []

    for j in range(0,len(cols)):
        cols_data.append(cols[j].text.encode("utf-8"))
        result_data.append(cols_data)
    print(result_data)

#finding name field using xpath
name = driver.find_element("xpath","//input[@id='name']")
name.send_keys("Jai Ram ji ki")

email = driver.find_element("xpath","//input[@name='email']")
email.send_keys("jaibajrangbali@gmail.com")

phone = driver.find_element("id","phone")
phone.send_keys("8448484848")

#Setting a dropdown

driver.find_element("xpath","//button[@data-toggle='dropdown']").click()
time.sleep(1)

#finding particular option and clicking on it
driver.find_element("xpath","//a[text()='Male']").click()

#setting a checkbox
checkbox = driver.find_element("xpath","//input[@type='checkbox']")
checkbox.click()

driver.save_screenshot("Screenshot/interaction.png")

#identifying path for click me button and clicking on it
button = driver.find_element("xpath","//button[text()='Click me!']")
button.click()

#pause screen for few sec
time.sleep(3)

#verifying user is redirecting another specific tutorial page
if(driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect'):
   print("success")
else:
    print("failure")

time.sleep(3)

driver.close()
