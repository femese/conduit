from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import pytest
import csv

browser_options = Options()
browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser_options.headless = True
URL = 'http://localhost:1667'

class Test_Setup:

    def test_setup(self):
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        browser.maximize_window()
        browser.get(URL)
        homepage = HomePage(browser)
        homepage.registration_button.click()
        registration_page = RegistrationPage(browser)
        user = ('Teszt User', 'teszt@teszt.com', 'Teszt1teszt')
        registration_page.fill_registration_details(user)
        registration_page.signup_button.click()
        homepage.success_ring.find()
        browser.get(URL)
        reader = csv.reader(open('../../vizsgaremek/articles.csv', 'r'), delimiter=';')
        for row in reader:
            navigation_bar = NavigationBar(browser)
            navigation_bar.logout_button.find()
            navigation_bar.article_button.click()
            new_article_page = NewArticlePage(browser)
            new_article_page.title_input.send_text_to_input(row[0])
            new_article_page.summary_input.send_text_to_input(row[1])
            new_article_page.main_body_input.send_text_to_input(row[2])
            new_article_page.tags_input.send_text_to_input(row[3])
            new_article_page.publish_button.click()
        navigation_bar.home_button.click()
        browser.close()
