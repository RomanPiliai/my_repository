import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.Dashboard_match import Dashboard_match

class TestAddMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    def test_add_match(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_button()
        add_match_page = Dashboard_match(self.driver)
        add_match_page.test_last_match()
        add_match_page.test_matches_button()
        add_match_page.test_click_add_match_button()
        add_match_page.test_type_in_my_team()
        add_match_page.test_type_in_enemy_team()
        add_match_page.test_type_my_score()
        add_match_page.test_type_in_enemy_score()
        add_match_page.test_type_in_date_match()
        add_match_page.test_click_submit_match_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()