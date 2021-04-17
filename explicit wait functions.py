# This test is written to show how we can use "Wait"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/earth/')

# wait until the element we want to interact with will be clickable
wait = WebDriverWait(driver, 10)

LaunchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span' )))
LaunchEarthButton.click()
