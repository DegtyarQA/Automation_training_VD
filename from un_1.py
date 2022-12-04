from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Valery")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Degtyar")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("Smolensk@minsk.by")
    input4 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    input4.send_keys("+375291230050")
    input5 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
    input5.send_keys("Veselovo")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    param = browser.find_element(By.CSS_SELECTOR, "div h1")
    x = str(param.text)
    assert "Congratulations! You have successfully registered!" == x, "Warning!!! ERROR!!"

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла