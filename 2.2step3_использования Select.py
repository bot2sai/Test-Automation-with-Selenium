
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/selects2.html'
    browser.get(url)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    res = int(num1)+int(num2)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(res))  
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
    time.sleep(10)


