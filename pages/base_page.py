from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def type_in_email(self, email):
        return self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        return self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)
