from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.article_page import ArticlePage
from pages.new_article_page import NewArticlePage
from pages.navigation_bar import NavigationBar
import pytest
import csv

browser_options = Options()
browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser_options.headless = True
URL = 'http://localhost:1667'

class Test_Conduit_Logged_In:

    def setup_method(self, method):
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)
        self.homepage = HomePage(driver=self.browser)
        self.homepage.login_button.click()
        login_page = LoginPage(driver=self.browser)
        login_page.fill_login_details('teszt@teszt.com', 'Teszt1teszt')
        login_page.signin_button.click()

    def teardown_method(self, method):
        self.browser.close()
        
    def test_one_article(self):
        self.homepage = HomePage(driver=self.browser)
        self.homepage.logout_button.find()
        self.homepage.article_button.click()
        new_article_page = NewArticlePage(driver=self.browser)
        new_article_page.title_input.send_text_to_input("Title")
        new_article_page.summary_input.send_text_to_input("Summary")
        new_article_page.main_body_input.send_text_to_input("Main article")
        new_article_page.tags_input.send_text_to_input("nonsense")
        new_article_page.publish_button.click()
        article_page = ArticlePage(driver=self.browser)
        assert article_page.main_textfield.text() == "Main article"

    def test_new_articles(self):
        number_of_paginator = len(self.homepage.page_list_buttons)
        reader = csv.reader(open('./vizsgaremek/articles.csv', 'r'), delimiter=';')
        for row in reader:
            navigation_bar = NavigationBar(driver=self.browser)
            navigation_bar.logout_button.find()
            navigation_bar.article_button.click()
            new_article_page = NewArticlePage(driver=self.browser)
            new_article_page.title_input.send_text_to_input(row[0])
            new_article_page.summary_input.send_text_to_input(row[1])
            new_article_page.main_body_input.send_text_to_input(row[2])
            new_article_page.tags_input.send_text_to_input(row[3])
            new_article_page.publish_button.click()
        navigation_bar.home_button.click()
        reader.close()
        assert len(self.homepage.page_list_buttons) > number_of_paginator

    def test_page_list(self):
        self.homepage = HomePage(driver=self.browser)
        for x in self.homepage.page_list_buttons:
            x.click()
            self.homepage = HomePage(driver=self.browser)
        assert self.homepage.is_last_page_active()

    def test_list_articles(self):
        print("Articles found on the page: " + str(len(self.homepage.article_list)))
        assert len(self.homepage.article_list) > 0

    def test_change_article(self):        
        self.homepage.profile_button.click()
        profile_page = ProfilePage(self.browser)
        self.homepage.article_list[0].click()
        article_page = ArticlePage(self.browser)
        txt_to_change = article_page.main_textfield.text()
        article_page.edit_button.find()
        article_page.edit_button.click()
        article_edit_page = NewArticlePage(self.browser)
        article_edit_page.main_body_input.send_text_to_input(txt_to_change[:len(txt_to_change)//2].strip() + "changed")
        article_edit_page.publish_button.click()
        assert article_page.main_textfield.text() == txt_to_change[:len(txt_to_change)//2].strip() + "changed"
        
    def test_save_to_file(self):
        self.homepage.profile_button.click()
        profile_page = ProfilePage(self.browser)
        self.homepage.article_list[0].click()
        article_page = ArticlePage(self.browser)
        txt_to_save = article_page.main_textfield.text()
        txt_file = open("./vizsgaremek/test.txt", "w")
        txt_file.write(txt_to_save)
        txt_file.close()
        txt_file = open("./vizsgaremek/test.txt", "r")
        assert txt_file.read() == txt_to_save
        txt_file.close()

    def test_delete_article(self):
        self.homepage.profile_button.click()
        profile_page = ProfilePage(self.browser)
        profile_page.article_list[0].click()
        article_page = ArticlePage(self.browser)
        article_page.delete_button.find()
        article_page.delete_button.click()
        assert (article_page.delete_popup.text() == "Deleted the article. Going home...")
        
    def test_logout(self):
        self.homepage.logout_button.click()
        assert self.homepage.login_button.text().strip() == "Sign in"