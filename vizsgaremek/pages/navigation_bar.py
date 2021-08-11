from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_element import BaseElement

class NavigationBar:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[1]")
    
    @property
    def login_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[2]")

    @property
    def registration_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[3]")

    @property
    def article_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[2]")

    @property
    def profile_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[4]")

    @property
    def logout_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//li[5]")