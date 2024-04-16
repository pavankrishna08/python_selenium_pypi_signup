from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()
url = 'https://www.techlistic.com/p/selenium-practice-form.html'

class DemoTesting(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = browser
        browser.maximize_window()
        browser.get(url)
        browser.implicitly_wait(30)

    def tearDown(self) -> None:
        browser.quit()

    def test_automate_form(self):
        first_name = browser.find_element(By.NAME,'firstname')
        first_name.send_keys('pavan')

        last_name = browser.find_element(By.NAME, 'lastname')
        last_name.send_keys('krishna')

        gender = browser.find_element(By.ID,'sex-1')
        print(gender.is_selected())
        gender.click()



