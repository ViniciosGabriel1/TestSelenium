from selenium import webdriver
import time

browser = webdriver.Edge()
browser.maximize_window()

browser.get("https://www.google.com.br/")
time.sleep(5)

browser.refresh()

browser.get("https://www.saucedemo.com/v1/")
time.sleep(2)

browser.back()
time.sleep(3)

browser.forward()
time.sleep(3)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")

time.sleep(3)

browser.quit()
time.sleep(4)




