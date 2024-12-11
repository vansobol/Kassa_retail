import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import logging
from pages.add_kkt import add_kkt
@pytest.mark.parametrize("driver_setup", ["ZY22DVMDXJ"], indirect=True)
def test_emulator(driver_setup):
    driver, udid = driver_setup
    add_kkt_page = add_kkt(driver)
    add_kkt_page.add_kkt()

    button_next = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_next'))
    button_next.click()
    name_kkt = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH, "//android.widget.FrameLayout / android.widget.EditText"))
    name_kkt.send_keys('1')
    save = add_kkt_page.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_save'))
    save.click()
    try:
        button_back = add_kkt_page.helper.short_wait_present((AppiumBy.XPATH, '//android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton'))
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

    kassa = add_kkt_page.helper.wait_visible((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_recycler_view"]/android.view.ViewGroup[1]'))
    kassa.click()
    kassa_sale = add_kkt_page.helper.wait_clickable((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_name" and @text="Приход"]' ))
    kassa_sale.click()