from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    namee = browser.find_element(By.NAME, 'firstname')
    namee.send_keys('Valery')
    surname = browser.find_element(By.NAME, 'lastname')
    surname.send_keys('Degtyar')
    mail = browser.find_element(By.NAME, 'email')
    mail.send_keys('Valery@lalery.valery')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'rekviem.txt')
    gruzim = browser.find_element(By.ID,'file')
    gruzim.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()