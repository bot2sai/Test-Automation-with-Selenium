import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def res(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/math.html'
    browser.get(url)
    res_value = browser.find_element(By.ID, 'input_value').text
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(res(res_value))
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()    
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
    time.sleep(10)


