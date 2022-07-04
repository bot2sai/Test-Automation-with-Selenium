import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def res(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()
alert = browser.switch_to.alert 
alert.accept()

answer = browser.find_element(By.ID, 'input_value').text
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(res(answer))
button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()

time.sleep(5)