from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(12)
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")


dropodown_sites = Select(browser.find_element(By.XPATH, '//select[@id = "first"]'))
dropodown_sites.select_by_value("Yahoo")
time.sleep(3)

dropdown_animal = Select(browser.find_element(By.XPATH, '//select[@id = "animals"]'))
dropdown_animal.select_by_visible_text("Avatar")
time.sleep(3)

dropdown_multiple = Select(browser.find_element(By.XPATH, '//select[@id = "second"]'))
dropdown_multiple.select_by_visible_text("Pizza")
time.sleep(3)
dropdown_multiple = Select(browser.find_element(By.XPATH, '//select[@id = "second"]'))
dropdown_multiple.select_by_visible_text("Burger")
time.sleep(3)
