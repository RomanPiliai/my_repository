from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//child::div/button/span[1]"
    remind_password_button_xpath = "//*[text()='Remind password']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_button_xpath = "// child::div[2] // a[1] / button / span[1]"
    expected_title_player = 'Add player'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_player_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title_player
