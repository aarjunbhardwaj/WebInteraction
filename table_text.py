import time
from selenium import webdriver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")

#getting the text in each cell of the table
# Finding the Example table element in the page
table = driver.find_element("xpath","//table[@name='Example Table']")

#using find_elements_by_xpath method to get the rows in the table
rows = table.find_elements("xpath","//tbody/descendant::tr")
#creating list[] to store the data
res_data =[]

# Going to each row and get the no of columns and the navigating to column
# Then getting the text from each column
for i in range(0,len(rows)):
    cols = rows[i].find_elements("tag name","td")
    cols_data = []
    for j in range(0,len(cols)):
        cols_data.append(cols[j].text.encode('utf-8'))
    res_data.append(cols_data)

print(res_data)

time.sleep(3)

driver.close()



