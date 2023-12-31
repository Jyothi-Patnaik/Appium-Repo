from Pages.BasePage import BasePage
from Pages.LoginScreen import LoginScreen
from Pages.SignUp import Sign_Up


class Test_CompanySignUp(BasePage):
    def test_signUp(self,appium_driver):
        self.lp = LoginScreen(self.driver)
        self.lp.setUsername("meera@yopmail.com")
        self.lp.setpassword("Inlink@123")
        self.lp.clickLogin()
        self.sp = Sign_Up(self.driver)
        self.sp.signUpClick()
        self.sp.companySignUpClick()
