import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

class PayPage:
    def __init__(self, webdriver_helper):
        self.webdriver_helper = webdriver_helper

    def non_cash_payment(self):
        try:
            non_cash = self.webdriver_helper.wait_present((AppiumBy.XPATH, '//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'))
            non_cash.click()
        except Exception:
            error = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)

        sno = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system'))
        sno.click()
        sno_select = self.webdriver_helper.wait_visible((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]'))
        sno_select.click()
        button_pay = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay'))
        button_pay.click()

    def cash_payment(self):
        try:
            without_change = self.webdriver_helper.wait_present((AppiumBy.XPATH, "//android.widget.Button[@text='Без сдачи']"))
            without_change.click()
            sno = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system'))
            sno.click()
            sno_select = self.webdriver_helper.wait_visible((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]'))
            sno_select.click()
            button_pay = self.webdriver_helper.wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay'))
            button_pay.click()
        except Exception:
            error = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(text)