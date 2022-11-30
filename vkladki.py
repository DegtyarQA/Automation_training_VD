from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin
from math import log
def fun(x):
    return log(abs(12*sin(x)))

link='http://suninjuly.github.io/redirect_accept.html'

try:
    browser  =webdriver.Chrome()
    browser.get(link)
    plaha = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
    plaha.click()
    w1 = browser.window_handles[1]
    browser.switch_to.window(w1)
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


