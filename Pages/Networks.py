from appium.webdriver.common.appiumby import AppiumBy


class Networks_Module:
    button_Networks_accId = 'Networks'
    button_Search_accId = 'Search…'
    text_SearchField_Id = 'com.peoplelink.inlink:id/search_src_text'

    def __init__(self, driver):
        self.driver = driver

    def clickNetworks(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.button_Networks_accId).click()

    def clickSearch_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.button_Search_accId).click()

    def searchCompany(self):
        self.driver.find_element(AppiumBy.ID, self.text_SearchField_Id).send_keys()
