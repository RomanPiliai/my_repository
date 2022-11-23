import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage

class TestLoginPageLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_language(self):
        user_login = LoginPage(self.driver)
        user_login.click_language_button()
        user_login.click_polski_language()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
