from selenium import webdriver

import time

from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()

browser.get("https://www.saucedemo.com/v1/")

# find_element

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")

# send_keys
time.sleep(3)
username.send_keys("standard_user")
time.sleep(3)
password.send_keys("secret_sauce")
time.sleep(3)

# find_elements
auth_fields = browser.find_elements(By.XPATH, '//*[@class="form_input"]')
print(auth_fields)
print(len(auth_fields))

assert len(auth_fields) == 1, "error"


browser.quit()

