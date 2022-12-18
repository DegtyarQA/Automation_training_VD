import pytest
from selenium.webdriver.common.by import By
import time
import math

answer = math.log(int(time.time()))

@pytest.mark.parametrize('link',
                         ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_login_page(browser, link):
    browser.get(link)
    time.sleep(15)
    log = browser.find_element(By.ID, 'ember33')
    log.click()
    enter1 = browser.find_element(By.NAME, 'login')
    enter1.send_keys("degtyar060589@gmail.com")
    enter2 = browser.find_element(By.NAME, 'password')
    enter2.send_keys("Arinula1618")
    button1 = browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
    button1.click()
    time.sleep(15)
    otvet = browser.find_element(By.ID, 'ember91')
    otvet.send_keys(answer)
    otpravka = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    otpravka.click()
    time.sleep(15)
    poisk = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    itog = str(poisk.text)
    assert itog=='Correct!', "Mimo"



