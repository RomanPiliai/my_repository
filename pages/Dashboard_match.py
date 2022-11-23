from pages.base_page import BasePage
from datetime import datetime

class Dashboard_match(BasePage):


    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//child::div/button/span[1]"
    remind_password_button_xpath = "//*[text()='Remind password']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    last_match_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]'
    my_team_input_xpath = "// *[ @ name = 'myTeam']"
    enemy_team_input_xpath = "// *[ @ name = 'enemyTeam']"
    my_team_score_input_xpath = "// *[ @ name = 'myTeamScore']"
    enemy_team_score_input_xpath = "// *[ @ name = 'enemyTeamScore']"
    date_input_xpath = "// *[ @ name = 'date']"
    match_at_home_checkmark_xpath = "// child:: div/label[1]/span[2]"
    match_out_home_checkmark_xpath = "// child:: div/label[2]/span[2]"
    submit_button_xpath = "// child:: div[3] / button[1] / span[1]"
    clear_button_xpath = "// child:: div[3] / button[2] / span[1]"
    matches_button_xpath = "// child:: div / ul[2] / div[2] / div[2] / span"
    reports_button_xpath = "// child:: div / ul[2] / div[3] / div[2] / span"
    sign_out_button_xpath = "// child:: div / ul[3] / div[2] / div[2] / span"
    add_match_button_xpath = '//*[@id="__next"]/div[1]/main/a/button/span[1]'
    my_team = 'Liverpool'
    enemy_team = 'Manchester City'
    my_team_score = '2'
    enemy_team_score = '1'
    date_input = datetime(2020, 2, 2)
    full_date = date_input.strftime("%m-%d-%Y")

    def test_type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def test_type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def test_click_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def test_last_match(self):
        self.click_on_the_element(self.last_match_button_xpath)

    def test_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)

    def test_click_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def test_type_in_my_team(self):
        self.field_send_keys(self.my_team_input_xpath, value=self.my_team)

    def test_type_in_enemy_team(self):
        self.field_send_keys(self.enemy_team_input_xpath, value=self.enemy_team)

    def test_type_in_enemy_score(self):
        self.field_send_keys(self.enemy_team_score_input_xpath, value=self.enemy_team_score)

    def test_type_my_score(self):
        self.field_send_keys(self.my_team_score_input_xpath, value=self.my_team_score)

    def test_type_in_date_match(self):
        self.field_send_keys(self.date_input_xpath, value=self.full_date)

    def test_click_submit_match_button(self):
        self.click_on_the_element(self.submit_button_xpath)
