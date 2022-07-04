import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def res(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
res_value = browser.find_element(By.ID, 'input_value').text
print(res_value)
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(res(res_value))

browser.execute_script("window.scrollBy(0, 200);")
input2 = browser.find_element(By.ID, 'robotCheckbox')
input2.click()    
input3 = browser.find_element(By.ID, 'robotsRule')
input3.click()
button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()
time.sleep(5)

