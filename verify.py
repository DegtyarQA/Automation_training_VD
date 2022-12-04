from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as CC
from selenium.webdriver.support.ui import WebDriverWait
import time
from math import sin
from math import log

def fun(x):
    return log(abs(12*sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    cost = WebDriverWait(browser, 15).until(CC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.ID, "book")
    button.click()
    param = browser.find_element(By.ID, "input_value")
    x = int(param.text)
    y = fun(x)
    enter = browser.find_element(By.ID, 'answer')
    enter.send_keys(y)
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
