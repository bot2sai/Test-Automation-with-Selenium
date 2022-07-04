import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def res(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(url)
    treasure = browser.find_element(By.ID, 'treasure')
    res_value= treasure.get_attribute('valuex')
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(res(res_value))

    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()    
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
    time.sleep(10)


