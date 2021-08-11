from selenium.webdriver.common.by import By
from pages.base_element import BaseElement

class ArticlePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def edit_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//*[contains(text(), 'Edit')]")

    @property
    def delete_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//*[contains(text(), 'Delete')]")

    @property
    def main_textfield(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//div/p")

    @property
    def delete_popup(self):
        return BaseElement(self.driver, By.XPATH, "//div[@class='swal-overlay swal-overlay--show-modal']")