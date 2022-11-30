from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin
from math import log
def fun(x):
    return log(abs(12*sin(x)))

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    knopka = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    knopka.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    param = browser.find_element(By.ID, "input_value")
    x = int(param.text)
    y = fun(x)
    enter = browser.find_element(By.ID, 'answer')
    enter.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
