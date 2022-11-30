from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sin
import time
from math import log
def fun(x):
    return log(abs(12*sin(x)))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    param=browser.find_element(By.ID, "input_value")
    x = int(param.text)
    y = fun(x)
    browser.execute_script("window.scrollBy(0, 100);")
    enter = browser.find_element(By.ID, 'answer')
    enter.send_keys(y)
    check1 = browser.find_element(By.ID, 'robotCheckbox')
    check1.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
