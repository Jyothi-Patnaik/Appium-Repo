import time

import pytest
import self
from appium.options.android import UiAutomator2Options
from appium.webdriver import webdriver

from appium.webdriver.common.appiumby import AppiumBy

from Pages.LoginScreen import LoginScreen


class BasePage:
    """def __init__(self,driver):
        self.driver = driver"""

    def appium_driver(self):
        desired_caps = dict(
            deviceName='emulator',
            platformName='Android',
            app='C://Users//admin//Downloads//inlink_test_30-11-2023 (1).apk',
            appPackage='com.peoplelink.inlink',
            automationName='uiAutomator2',
            fullReset='true',
            autoGrantPermissions='true'
        )
        Capabilities_Options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=Capabilities_Options)
        # request.cls.driver = driver
        driver.implicitly_wait(10)
        driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/skipBtn').click()
        driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/checkBox').click()
        ele = driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/continueBtn')
        ele.click()
        yield driver
        driver.quit()
