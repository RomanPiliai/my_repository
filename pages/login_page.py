from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//child::div/button/span[1]"
    remind_password_button_xpath = "//*[text()='Remind password']"
    language_selectMenu_xpath = "//child::div/div[2]/div/div"
    polski_selectMenu_xpath = "//*/div[3]/ul/li[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'


    email = "romanpiliai96@gmail.com"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_language_button(self):
        self.click_on_the_element(self.language_selectMenu_xpath)

    def click_polski_language(self):
        self.click_on_the_element(self.polski_selectMenu_xpath)