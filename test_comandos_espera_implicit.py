from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(12)

browser.get("https://chercher.tech/practice/implicit-wait-example")

checkbox = browser.find_element(By.XPATH, '(//input[@type = "checkbox"])[1]')
checkbox.click()
assert checkbox.is_displayed()
time.sleep(4)
print("CheckBox apareceu e foi marcado")



