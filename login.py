import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

link = 'https://stepik.org/lesson/236895/step/1'

def getpage(browser):
    browser.get(link)
    log = browser.find_element(By.ID, 'ember33')
    log.click
    print(ok)

"""@pytest.mark.parametrize('login, password', [("degtyar060589@gmail.com", "Arinula1618")])
def test_login(login, password, browser):
 enter1 = browser.find_element(By.NAME, 'login')
 enter1.send_keys(login)
 enter2 = browser.find_element(By.NAME, 'password')
 enter2.send_keys(password)
 button1=browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')
 button1.click()"""