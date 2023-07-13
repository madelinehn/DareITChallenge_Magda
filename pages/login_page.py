from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type, 'submit']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts Panel - sign in"
    title_of_box = "//*[id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"

    def type_in_email(self, email):
        return self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        return self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

