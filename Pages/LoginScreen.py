import self
from appium.webdriver.common.appiumby import AppiumBy


class LoginScreen:
    textbox_username_name = "com.peoplelink.inlink:id/emailET"
    textbox_password_name = "com.peoplelink.inlink:id/passwordET"
    button_login_xpath = "com.peoplelink.inlink:id/loginBtn"
    errorMessade_id = "com.peoplelink.inlink:id/errorTV"

    def __init__(self, driver):
        self.driver = driver

    def invalidEmailLogin(self, invalidEmail, password):
        self.driver.find_element(AppiumBy.ID, self.textbox_username_name).send_keys(invalidEmail)
        self.driver.find_element(AppiumBy.ID, self.textbox_password_name).send_keys(password)
        print("wrong email")

    def errorMsg(self):
        errorText = self.driver.find_element(AppiumBy.ID, self.errorMessade_id)
        actText = errorText.text
        expText = "Incorrect Username or Password"
        if actText == expText:
            print(actText)
        else:
            print("No error")

    def invalidPasswordLogin(self, username, invalidPassword):
        self.driver.find_element(AppiumBy.ID, self.textbox_username_name).send_keys(username)
        self.driver.find_element(AppiumBy.ID, self.textbox_password_name).send_keys(invalidPassword)
        print("\nwrong password")

    def validLogin(self, username, password):
        self.driver.find_element(AppiumBy.ID, self.textbox_username_name).send_keys(username)
        self.driver.find_element(AppiumBy.ID, self.textbox_password_name).send_keys(password)
        # self.type("email_XPATH", username)

    def caseSensitiveLogin(self, USERNAME, password):
        self.driver.find_element(AppiumBy.ID, self.textbox_username_name).send_keys(USERNAME)
        self.driver.find_element(AppiumBy.ID, self.textbox_password_name).send_keys(password)
        print("successful login with case sensitive Email")

    def clickLogin(self):
        self.driver.find_element(AppiumBy.ID, self.button_login_xpath).click()

    def loginTextValidation(self):
        title1 = self.driver.find_element(AppiumBy.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView')
        text1 = title1.text
        expTitle = "Meera Industries Pvt Ltd"
        if text1 == expTitle:
            print(text1)
        else:
            print("error")
