from pages.base_page import BasePage
from datetime import datetime

class AddPlayer(BasePage):

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//child::div/button/span[1]"
    remind_password_button_xpath = "//*[text()='Remind password']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_button_xpath = "// child::div[2] // a[1] / button / span[1]"
    expected_title_player = 'Add player'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    input_name_xpath = '//*/div[2]/div/div/input'
    input_surname_xpath = '//*/div[3]/div/div/input'
    input_age_xpath = '//*/div[7]/div/div/input'
    input_position_xpath = '//*/div[11]/div/div/input'
    submit_button_xpath = '//*/div[3]/button[1]/span[1]'
    name = 'Aureliano'
    surname = 'Buendia'
    position = 'Goalkeeper'
    age = datetime(1899, 2, 21)
    age_date = age.strftime("%m-%d-%Y")


    def test_type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def test_type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def test_click_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def test_click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def test_type_in_name(self):
        self.field_send_keys(self.input_name_xpath, value=self.name)

    def test_type_in_surname(self):
        self.field_send_keys(self.input_surname_xpath, value=self.surname)

    def test_type_in_position(self):
        self.field_send_keys(self.input_position_xpath, value=self.position)

    def test_type_in_age(self):
        self.field_send_keys(self.input_age_xpath, value=self.age_date)

    def test_click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
