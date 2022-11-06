from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//child::div/button/span[1]"
    remind_password_button_xpath = "//*[text()='Remind password']"
    language_selectMenu_xpath = "//*[text()='English']"
    email = "romanpiliai96@gmail.com"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
