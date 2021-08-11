from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_element import BaseElement
from pages.navigation_bar import NavigationBar

class HomePage(NavigationBar):
    def __init__(self, driver):
        self.driver = driver

    @property
    def cookie_link(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//a [@href='https://cookiesandyou.com/']")

    @property
    def cookie_accept(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//*[contains(text(), 'I accept!')]")

    @property
    def page_numbers(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//a[@class='page-link']")

    @property
    def success_ring(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//div[@class='swal-icon--success__ring']")

    @property
    def success_text(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//div[@class='swal-text']")

    @property
    def success_button(self):
        return BaseElement(driver=self.driver, by=By.XPATH, value="//div[@class='swal-button-container']/button")

    def cookie_absent(self):
        cookie_accept_locator = (By.XPATH, "//*[contains(text(), 'I accept!')]")
        WebDriverWait(self.driver, 10, 2).until(EC.invisibility_of_element_located(cookie_accept_locator))
        return len(self.driver.find_elements(*cookie_accept_locator)) == 0

    @property
    def page_list_buttons(self):
        page_list = []
        WebDriverWait(self.driver, 10, 2).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='pagination']/li")))
        for i in range(len(self.driver.find_elements(By.XPATH, "//ul[@class='pagination']/li"))):
            xpath = "//ul[@class='pagination']/li[" + str(i+1) + "]/a"
            page_list.append(BaseElement(self.driver, By.XPATH, xpath))
        return page_list

    @property
    def article_list(self):
        article_list = []
        WebDriverWait(self.driver, 10, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='article-preview']")))
        for i in range(len(self.driver.find_elements(By.XPATH, "//div[@class='article-preview']"))):
            xpath = "//div[@class='article-preview'][" + str(i + 1) + "]/a"
            article_list.append(BaseElement(self.driver, By.XPATH, xpath))
        return article_list

    def is_last_page_active(self):
        last_number = len(self.driver.find_elements(By.XPATH, "//ul[@class='pagination']/li"))
        xpath = "//ul[@class='pagination']/li[" + str(last_number) +"]"
        return self.driver.find_element_by_xpath(xpath).get_attribute("class") == "page-item active"