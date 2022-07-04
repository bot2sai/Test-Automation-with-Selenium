import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
input1.send_keys('Андрей')
input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
input2.send_keys('Георгиевский')   
input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
input3.send_keys('lol@mil.ru')   
input4 = browser.find_element(By.ID, 'file')
# input4.send_keys('C:/Users/Slytherin/Desktop/Python, SQL/Тестирование/Автоматизация тестирования с помощью Selenium и Python/text.txt') 
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
input4.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
button.click()
time.sleep(5)