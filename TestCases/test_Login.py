import pytest

import time

from Pages.LoginScreen import LoginScreen
from Pages.BasePage import BasePage


# class Test_LoginApp(BaseTest):
class Test_001_Login(BasePage):
    username = "meera@yopmail.com"
    password = "Inlink@123"
    invalidEmail = "meerayopmail.com"
    invalidPassword = "Inlink123"
    USERNAME = "MEERA@YOPMAIL.COM"


    def test_loginScenarios(self, appium_driver):
        # self.driver = webdriver.Remote('http://appium.server:4723/wd/hub', desired_capabilities=desired_caps)

        self.lp = LoginScreen(self.driver)
        time.sleep(2)
        self.lp.invalidEmailLogin(self.invalidEmail, self.password)
        self.lp.clickLogin()
        self.lp.errorMsg()
        time.sleep(3)
        self.lp.invalidPasswordLogin(self.username, self.invalidPassword)
        self.lp.clickLogin()
        self.lp.errorMsg()
        time.sleep(2)
        self.lp.caseSensitiveLogin(self.USERNAME, self.password)
        self.lp.clickLogin()
        time.sleep(2)

    def test_loginValid(self, appium_driver):
        self.lp1 = LoginScreen(self.driver)
        self.lp1.validLogin(self.username, self.password)
        self.lp1.clickLogin()
        time.sleep(10)
        self.lp1.loginTextValidation()
