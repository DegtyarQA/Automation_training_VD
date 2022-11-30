from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    cifra_1 = browser.find_element(By.ID, 'num1')
    c1 = int(cifra_1.text)
    cifra_2 = browser.find_element(By.ID, 'num2')
    c2 = int(cifra_2.text)
    c = c1+ c2
    z=str(c)
    sel=Select(browser.find_element(By.ID,'dropdown'))
    sel.select_by_visible_text(z)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()