import time
from selenium import webdriver
from selenium.webdriver import ActionChains

edge = webdriver.Edge()
edge.maximize_window()

edge.get("http://qxf2.com/selenium-tutorial-main")

#locating the menu and clicking on that
menu = edge.find_element("xpath","//img[@src='./assets/img/menu.png']")
menu.click()

#locating the resource element to hover over
element = edge.find_element("xpath","//a[text()='Resources']")

#Use ActionChains to hover over elements
action = ActionChains(edge)
action.move_to_element(element)
action.perform()
time.sleep(2) #Adding waits to make the example more visual

# Clicking the GUI automation link
gui_automation = edge.find_element("xpath","//a[text()='GUI automation']")
gui_automation.click()

time.sleep(3)
edge.close()

