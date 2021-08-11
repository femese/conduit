from selenium.webdriver.common.by import By
from pages.base_element import BaseElement

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def email_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//input[@placeholder='Email']")

    @property
    def password_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//input[@placeholder='Password']")

    @property
    def signin_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//button[1]")

    def fill_login_details(self, email, password):
        self.email_input.send_text_to_input(email)
        self.password_input.send_text_to_input(password)