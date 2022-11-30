from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/get_attribute.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    sunduk = browser.find_element(By.CSS_SELECTOR, '[src="images/chest.png"]')
    klad = sunduk.get_attribute('valuex')
    x=klad
    y=calc(x)
    enter = browser.find_element(By.ID, 'answer')
    enter.send_keys(y)
    check1 = browser.find_element(By.ID, 'robotCheckbox')
    check1.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR,'.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()


