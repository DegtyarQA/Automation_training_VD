import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)
    enter = browser.find_element(By.ID, 'answer')
    enter.send_keys(y)
    check1 = browser.find_element(By.ID, 'robotCheckbox')
    check1.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR,'.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

