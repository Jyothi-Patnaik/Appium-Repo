from appium.webdriver.common.appiumby import AppiumBy


class Sign_Up:
    signUp_btn_id = 'com.peoplelink.inlink:id/signupBtn'
    company_signUp_btn_id = 'com.peoplelink.inlink:id/company_signup'

    # button_login_xpath = "com.peoplelink.inlink:id/loginBtn"

    def __init__(self, driver):
        self.driver = driver

    def signUpClick(self):
        self.driver.find_element(AppiumBy.ID, self.signUp_btn_id).click()

    def companySignUpClick(self):
        self.driver.find_element(AppiumBy.ID, self.company_signUp_btn_id).click()
