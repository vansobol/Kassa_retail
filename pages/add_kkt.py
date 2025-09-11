from appium.webdriver.common.appiumby import AppiumBy
import time
from driver_helper import WebDriverHelper
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import logging

class addKkt:
    def __init__(self, driver):
        self.driver = driver
        self.helper = WebDriverHelper(driver)

    def add_kkt(self):
        side_menu = self.helper.wait_present((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
        side_menu.click()
        time.sleep(1)
        self.driver.swipe(100, 2000, 100, 600, duration=1500)

        settings = self.helper.short_wait_present((AppiumBy.XPATH, "//android.widget.TextView[@text='Настройки']"))
        settings.click()

        kkt_settings = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_kkt_name'))
        kkt_settings.click()

        add_kkt = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_add'))
        add_kkt.click()

    def save_kkt(self):
        save = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_save'))
        save.click()
        try:
            button_back = self.helper.short_wait_present((AppiumBy.XPATH,
                                                                  '//android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton'))
            button_back.click()
        except NoSuchElementException:
            error = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)
        except TimeoutException:
            error = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)
        except Exception:
            logging.info('Непредвиденная ошибка')
        try:
            side_menu = self.helper.short_wait_present((AppiumBy.ACCESSIBILITY_ID, 'Open'))
            side_menu.click()
        except NoSuchElementException:
            error = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)
        except TimeoutException:
            error = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)
        except Exception:
            logging.info('Непредвиденная ошибка')