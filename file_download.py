from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link='http://suninjuly.github.io/file_input.html'
    browser=webdriver.Chrome()
    browser.get(link)
    namee = browser.find_element(By.NAME, 'firstname')
    namee.send_keys('Valery')
    surname = browser.find_element(By.NAME, 'lastname')
    surname.send_keys('Degtyar')
    mail = browser.find_element(By.NAME, 'email')
    namee.send_keys('Valery@lalery.valery')
    
