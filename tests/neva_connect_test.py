import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import logging
from pages.add_kkt import add_kkt

@pytest.mark.parametrize("driver_setup", ["1043b195"], indirect=True)
def test_neva(driver_setup):
    driver, udid = driver_setup
    add_kkt_page = add_kkt(driver)
    add_kkt_page.add_kkt()

    select_vendor = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'))
    select_vendor.click()

    select_armax = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH,'//android.widget.LinearLayout[13]/android.widget.RelativeLayout/android.widget.TextView'))
    select_armax.click()

    button_next = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_next'))
    button_next.click()

    save = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_save'))
    save.click()
    try:
        button_back = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH,'//android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton'))
        button_back.click()
    except NoSuchElementException:
        error = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
        text = error.text
        logging.info(text)
    except TimeoutException:
        error = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
        text = error.text
        logging.info(text)
    except Exception:
        logging.info('Непредвиденная ошибка')
    try:
        side_menu = add_kkt_page.helper.short_wait_present((AppiumBy.ACCESSIBILITY_ID, 'Open'))
        side_menu.click()
    except NoSuchElementException:
        error = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
        text = error.text
        logging.info(text)
    except TimeoutException:
        error = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
        text = error.text
        logging.info(text)
    except Exception:
        logging.info('Непредвиденная ошибка')