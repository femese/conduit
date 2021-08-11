from selenium.webdriver.common.by import By
from pages.base_element import BaseElement
from pages.navigation_bar import NavigationBar
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(NavigationBar):
    def __init__(self, driver):
        self.driver = driver
        
    @property
    def article_list(self):
        article_list = []
        WebDriverWait(self.driver, 10, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='article-preview']")))
        for i in range(len(self.driver.find_elements(By.XPATH, "//div[@class='article-preview']"))):
            xpath = "//div[@class='article-preview'][" + str(i + 1) + "]/a"
            article_list.append(BaseElement(self.driver, By.XPATH, xpath))
        return article_list

    @property
    def page_list_buttons(self):
        page_list = []
        WebDriverWait(self.driver, 10, 2).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='pagination']/li")))
        for i in range(len(self.driver.find_elements(By.XPATH, "//ul[@class='pagination']/li"))):
            xpath = "//ul[@class='pagination']/li[" + str(i+1) + "]/a"
            page_list.append(BaseElement(self.driver, By.XPATH, xpath))
        return page_list