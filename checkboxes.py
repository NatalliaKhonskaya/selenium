# This test is written to automate basic functionality of any website:
# checkboxes
# and also make an assertion

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

# check the checkbox
checkbox = driver.find_element_by_xpath('//*[@id="isAgeSelected"]')
checkbox.click()

# make an assertion that after checking a checkbox we have the particular message
element = driver.find_element_by_xpath('//*[@id="txtAge"]').text
assert element == 'Success - Check box is checked'

#___________________________________________________________________________________________#

# click on the button that checks all checkboxes on the page
checkAllButton = driver.find_element_by_xpath('//*[@id="check1"]')
checkAllButton.click()

# verify that all checkboxes are checked, and if they are checked we get a message about it
checkbox1 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input')
if checkbox1.is_selected():
    print('checkbox1 is selected')

checkbox2 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label/input')
if checkbox2.is_selected():
    print('checkbox2 is selected')

checkbox3 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
if checkbox3.is_selected():
    print('checkbox3 is selected')

checkbox4 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
if checkbox4.is_selected():
    print('checkbox4 is selected')

