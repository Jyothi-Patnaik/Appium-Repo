import time

from Pages.BasePage import BasePage
from Pages.LoginScreen import LoginScreen
from Pages.Networks import Networks_Module


class Test_Networks(BasePage):
    search_Company="Two Company"

    def test_Networks(self, appium_driver):
        self.lp = LoginScreen(self.driver)
        self.lp.validLogin("meera@yopmail.com","Inlink@123")
        self.lp.clickLogin()
        time.sleep(5)
        self.nw = Networks_Module(self.driver)
        self.nw.clickNetworks()
        time.sleep(5)
        self.nw.clickSearch_button()
        time.sleep(5)
        self.nw.searchCompany()

