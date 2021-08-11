from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import pytest
import random
import string

browser_options = Options()
browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser_options.headless = True
URL = 'http://localhost:1667'

class Test_Conduit:

    def setup_method(self, method):
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)
        self.homepage = HomePage(driver=self.browser)

    def teardown_method(self, method):
        self.browser.close()

    def test_registration(self):
        self.homepage.registration_button.click()        
        registration_page = RegistrationPage(driver=self.browser)        
        registration_page.fill_registration_details(self.create_random_user())
        registration_page.signup_button.click()
        self.homepage.success_ring.find()
        assert self.homepage.success_text.text() == "Your registration was successful!"

    def create_random_user(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        email = ''.join(random.choice(string.ascii_lowercase) for i in range(6)) + "@" \
                + ''.join(random.choice(string.ascii_lowercase) for i in range(5)) + ".com"
        password = ''.join(random.choice(string.ascii_letters) for i in range(7)) + str(random.randint(1, 9))
        return (username, email, password)

    def test_login(self):
        self.homepage.login_button.click()
        login_page = LoginPage(driver=self.browser)
        login_page.fill_login_details('teszt@teszt.com','Teszt1teszt')
        login_page.signin_button.click()
        assert self.homepage.logout_button.text().strip() == "Log out"

    def test_cookie(self):
        self.homepage.cookie_accept.find()
        self.homepage.cookie_accept.click()
        assert self.homepage.cookie_absent()
