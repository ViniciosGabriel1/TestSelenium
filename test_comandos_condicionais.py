from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()

browser.get("https://demo.applitools.com/")


username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")
checkbox_remember_me = browser.find_element(By.XPATH, '//*[@class = "form-check-input"]')


# is_disabled
username.is_displayed()
print(username.is_displayed())
assert username.is_displayed()

#is_enabled
username.is_enabled()
print(username.is_enabled())
assert username.is_enabled()

# is_selected
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

checkbox_remember_me.click()
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()

