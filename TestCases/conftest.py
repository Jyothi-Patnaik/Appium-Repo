import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

""""
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
"""


@pytest.fixture(scope="function")
def appium_driver(request):
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
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/skipBtn').click()
    driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/checkBox').click()
    ele = driver.find_element(AppiumBy.ID, 'com.peoplelink.inlink:id/continueBtn')
    ele.click()
    yield driver
    driver.quit()

""""
@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
"""