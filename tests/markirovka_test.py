import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time
from pages.add_mark_good import AddMarkGood
from pages.pay import PayPage
from driver_helper import WebDriverHelper
import logging

def test_markirovka(driver_setup):
    driver, udid = driver_setup
    driver_helper = WebDriverHelper(driver)
    pay_page = PayPage(driver_helper)
    add_mark_good = AddMarkGood(driver_helper)
    add_mark_good.close_search()
    add_mark_good.add_mark('04601653035829H;dV)bFACVUdGVz')
    # add_mark_good.add_mark('0000004621065422dBtACAAPidGVz')
    time.sleep(1)
    done = driver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done'))
    done.click()
    time.sleep(1)
    total = driver_helper.wait_visible((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue'))
    total.click()
    add_mark_good.mark_check()
    pay_page.cash_payment()




