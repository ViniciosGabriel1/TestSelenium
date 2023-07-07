from selenium import webdriver
import time

browser = webdriver.Edge()
browser.maximize_window()

browser.get("https://www.saucedemo.com/v1/")


#title
print(f"O título da página é {browser.title}")

#current_url
print(f"A url da pággina pe  {browser.current_url}")

#page_source
print(f"O código fonte da página é {browser.page_source}")