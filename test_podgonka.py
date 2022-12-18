import pytest
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link="https://stepik.org/lesson/236895/step/1"
def test_login_page(browser):
    browser.get(link)
    log = browser.find_element(By.ID, 'ember33')
    log.click()
    enter1 = browser.find_element(By.NAME, 'login')
    enter1.send_keys("degtyar060589@gmail.com")
    enter2 = browser.find_element(By.NAME, 'password')
    enter2.send_keys("Arinula1618")
    button1 = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
    button1.click()
    otvet = browser.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea')
    otvet.send_keys(str(math.log(int(time.time()))))
    time.sleep(5)
    otpravka = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    otpravka.click()
    time.sleep(5)
    poisk = browser.find_element(By.CSS_SELECTOR, ".smart-hints>.smart-hints__hint")
    time.sleep(5)
    itog = str(poisk.text)
    print(itog)

    """"poisk = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hismart-hints"))
    )
    itog = str(poisk.text)
    assert itog == 'Correct!', "Mimo"  """

