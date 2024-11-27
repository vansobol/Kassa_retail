import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

def test_markirovka(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 15)
    add_receipt_items = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item')))
    add_receipt_items.click()
    try:
        search_close = WebDriverWait(driver, 3).until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_close_btn')))
        search_close.click()
        search_close2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_close_btn')))
        search_close2.click()
    except TimeoutException:
        print("Элемент 'search_close'  не найден, продолжаем выполнение теста.")

    select_item = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)')))
    select_item.click()

    ActionChains(driver).send_keys("04601653035829H;dV)bFACVUdGVz").send_keys(Keys.ENTER).perform()

    select_item = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)')))
    select_item.click()

    ActionChains(driver).send_keys("0000004621065422dBtACAAPidGVz").send_keys(Keys.ENTER).perform()

    time.sleep(1)
    done = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done')))
    done.click()
    time.sleep(1)

    total = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    total.click()
    try:
        oism_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_ignore_oism_errors')))
        oism_button.click()
    except TimeoutException:
        print("окна проверки ЧЗ нет")
        pass
    without_change = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, ("//android.widget.Button[@text='Без сдачи']"))))
    without_change.click()
    sno = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system')))
    sno.click()
    sno_select = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    sno_select.click()
    # button_pay = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay')
    # button_pay.click()

