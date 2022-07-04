import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def result(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
res = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
button = browser.find_element(By.ID, 'book')
button.click()

answer1 = browser.find_element(By.ID, 'input_value').text
input1 = browser.find_element(By.ID, 'answer')
print(result(answer1))
input1.send_keys(result(answer1))
button1 = browser.find_element(By.ID, 'solve')
button1.click()

time.sleep(5)