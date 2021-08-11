from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.base_element import BaseElement

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def username(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//input[@type='text'])[1]")

    @property
    def email(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//input[@type='text'])[2]")

    @property
    def password(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//input[@type='password']")

    @property
    def signup_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//button)")
        
    def fill_registration_details(self, user):
        self.username.send_text_to_input(user[0])
        self.email.send_text_to_input(user[1])
        self.password.send_text_to_input(user[2])

        