from appium.webdriver.common.appiumby import AppiumBy

class LoyaltyPage:
    def __init__(self, webdriver_helper):
        self.webdriver_helper = webdriver_helper

    def perform_loyalty_actions(self):
        self.webdriver_helper.wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/image_receipt_discount')).click()

        self.webdriver_helper.wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add')).click()

        self.webdriver_helper.wait_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/loyaltyInput")')).send_keys("22222")

        self.webdriver_helper.wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/button_add").instance(1)')).click()

        self.webdriver_helper.wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add')).click()

        self.webdriver_helper.wait_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/loyaltyInput")')).send_keys("44444")

        self.webdriver_helper.wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/button_add").instance(1)')).click()

        self.webdriver_helper.wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Списать баллы")')).click()

        self.webdriver_helper.driver.press_keycode(12)
        self.webdriver_helper.driver.press_keycode(4)

        self.webdriver_helper.wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')).click()
