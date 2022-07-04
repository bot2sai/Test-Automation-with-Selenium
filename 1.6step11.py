from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("test11@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    input4.send_keys("3579631327")
    input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input4.send_keys("Где то в РФ")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)
