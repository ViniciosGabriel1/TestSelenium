from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(12)
browser.get("https://chercher.tech/practice/frames")


frame1 = browser.find_element(By.XPATH, '//iframe[@id="frame1"]')
browser.switch_to.frame(frame1)
browser.find_element(By.XPATH, '//*[@id ="topic"]/following-sibling::input').send_keys("iframe1")
time.sleep(3)

frame3 = browser.find_element(By.XPATH, '//iframe[@id="frame3"]')
browser.switch_to.frame(frame3)
checkbox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
checkbox.click()
time.sleep(3)

browser.switch_to.default_content()

frame2 = browser.find_element(By.XPATH, '//iframe[@id="frame2"]')
browser.switch_to.frame(frame2)
dropdown_animal = Select(browser.find_element(By.XPATH, '//select[@id = "animals"]'))
dropdown_animal.select_by_visible_text("Avatar")
time.sleep(3)




