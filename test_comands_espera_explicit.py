from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Edge()
browser.maximize_window()

browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
wait = WebDriverWait(browser, 25)

# Identifica se a mensagem de  alerta será exibido

alert_btn = browser.find_element(By.ID, "alert")
alert_btn.click()
wait.until(expected_conditions.alert_is_present())
time.sleep(3)

# Analisa se o texto foi mudado
change_button = browser.find_element(By.ID, "populate-text")
change_button.click()
wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, '//h2[@class="target-text"]'), "Selenium Webdriver" ))
target_text = browser.find_element(By.XPATH, '//h2[@class="target-text"]').text
assert target_text == "Selenium Webdriver", "error"
time.sleep(3)

# Espera o botão se tornar clicável
browser.find_element(By.ID, "display-other-button").click()
wait.until(expected_conditions.element_to_be_clickable((By.ID, "hidden")))
time.sleep(3)

browser.find_element(By.ID, "enable-button")

# Espera o checkbox ser marcado
aparacer = browser.find_element(By.ID, "checkbox")
aparacer.click()
wait.until(expected_conditions.element_to_be_selected((browser.find_element(By.ID, "ch"))))
time.sleep(2)














