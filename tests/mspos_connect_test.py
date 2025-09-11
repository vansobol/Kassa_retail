import pytest
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
import time
import logging
from pages.add_kkt import addKkt
@pytest.mark.parametrize("driver_setup", ["PE69225N40527"], indirect=True)
def test_mspos(driver_setup):
    driver, udid = driver_setup
    add_kkt_page = addKkt(driver)
    add_kkt_page.add_kkt()


    select_vendor = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'))
    select_vendor.click()

    select_mspos = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH,'//android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView'))
    select_mspos.click()

    button_next = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_next'))
    button_next.click()

    type_connect = add_kkt_page.helper.short_wait_present((AppiumBy.ID,'com.bifit.cashdesk.mobile:id/text_input_connection_type'))
    type_connect.click()
    time.sleep(1)
    select_type = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'android:id/content'))
    select_type.click()

    add_kkt_page.save_kkt()