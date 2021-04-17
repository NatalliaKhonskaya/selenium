# This test is written to automate basic functionality of any website:
# input fields, clicking buttons

from selenium import webdriver


# This lines of code is written because of pop-up window appeared on the website.
# So i need to wait for an element located on the page
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


# This lines of code is written because of pop-up window appeared on the website.
# So i need to wait for an element located on the page
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print ("Timed out waiting for page to load")

# this is the part of the website i waited for and subsequent location of the element to close the pop-up window
CloseButton = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
CloseButton.click()


#type Single Input Field
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello, Natalie')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

# type Single Input Field
EnterValueA = driver.find_element_by_xpath('//*[@id="sum1"]')
EnterValueA.send_keys('18')
EnterValueB = driver.find_element_by_xpath('//*[@id="sum2"]')
EnterValueB.send_keys('12')
GetTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
GetTotalButton.click()