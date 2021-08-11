from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def text(self):
        text = self.web_element.text
        return text

    def send_text_to_input(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None
