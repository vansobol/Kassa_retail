from driver_helper import WebDriverHelper
from selenium.common.exceptions import TimeoutException
import logging
from appium.webdriver.common.appiumby import AppiumBy

class SaleScreen:
    def __init__(self, driver):
        self.driver = driver
        self.helper = WebDriverHelper(driver)

    def swipe_up(self, duration=800):

            size = self.driver.get_window_size()
            w = size['width']
            h = size['height']

            # Свайп с 80% экрана до 20%
            self.driver.swipe(w // 2, int(h * 0.8), w // 2, int(h * 0.2), duration=duration)

    def close_banner(self):
            try:
                close_btn = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/closeBtn'))
                close_btn.click()
            except TimeoutException:
                logging.info("Уведомлений не обнаружено")