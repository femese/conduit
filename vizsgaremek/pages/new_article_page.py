from selenium.webdriver.common.by import By
from pages.base_element import BaseElement

class NewArticlePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def title_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//input[@type='text'])[1]")

    @property
    def summary_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//input[@type='text'])[2]")

    @property
    def main_body_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//textarea")

    @property
    def tags_input(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//input[@type='text'])[3]")

    @property
    def publish_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="(//button[@type='submit'])")