# This test is written to automate drag & drop functionality

from selenium import webdriver

# to perform drag & drop action we need to add an additional library
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# perform drag & drop action
source = driver.find_element_by_xpath('//*[@id="box7"]')
dest = driver.find_element_by_xpath('//*[@id="box107"]')
action = ActionChains(driver)
action.drag_and_drop(source, dest).perform()




