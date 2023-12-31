import time
from lib2to3.pgen2 import driver

from Pages.BasePage import BasePage
from Pages.LoginScreen import LoginScreen
from Pages.NewsFeed import News_Feed


class Test_NewsFeed_001(BasePage):
    textPost = "Python Page"
    textImagePost="Image Python"

    def test_createFeed(self, appium_driver):
        self.lp = LoginScreen(self.driver)
        self.lp.validLogin("meera@yopmail.com", "Inlink@123")
        self.lp.clickLogin()
        time.sleep(5)
        self.n = News_Feed(self.driver)
        time.sleep(3)
        self.n.createPost()
        time.sleep(3)
        self.n.text_post(self.textPost)
        self.n.upload_text_post()
        self.n.createPost()
        time.sleep(7)
        """"
        self.n.clickGallery_button()
        self.n.select_Image()
        self.n.click_done_button()
        self.n.text_post(self.textImagePost)
        self.n.upload_text_post()
        """
