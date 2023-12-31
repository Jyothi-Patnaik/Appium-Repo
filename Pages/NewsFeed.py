from appium.webdriver.common.appiumby import AppiumBy

from TestCases.test_Login import Test_001_Login


class News_Feed:
    button_createPost = "com.peoplelink.inlink:id/create_post"
    text_post_input_id = 'com.peoplelink.inlink:id/feed_description'
    post_button_id = "com.peoplelink.inlink:id/post_feed_btn"
    text_Title_xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView'
    gallery_button_id='com.peoplelink.inlink: id / gallery_picker'
    image1_selection_xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.TextView'
    image2_selection_xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.TextView'
    done_button_xpath='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.TextView'

    def __init__(self, driver):
        self.driver = driver

    def createPost(self):
        self.driver.find_element(AppiumBy.ID, self.button_createPost).click()

    def text_post(self, textPost):
        self.driver.find_element(AppiumBy.ID, self.text_post_input_id).send_keys(textPost)

    def upload_text_post(self):
        self.driver.find_element(AppiumBy.ID, self.post_button_id).click()
        title1 = self.driver.find_element(AppiumBy.XPATH,self.text_Title_xpath)
        text1 = title1.text
        print(text1)

    def clickGallery_button(self):
        self.driver.find_element(AppiumBy.ID,self.gallery_button_id)

    def select_Image(self):
        self.driver.find_element(AppiumBy.XPATH,self.image1_selection_xpath)
        self.driver.find_element(AppiumBy.XPATH,self.image2_selection_xpath)

    def click_done_button(self):
        self.driver.find_element(AppiumBy.XPATH,self.done_button_xpath)