import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer

class TestaAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.test_click_add_player_button()
        add_player_page.test_type_in_name()
        add_player_page.test_type_in_surname()
        add_player_page.test_type_in_position()
        add_player_page.test_type_in_age()
        add_player_page.test_click_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
