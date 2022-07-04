
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/huge_form.html'
    browser.get(url)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)


