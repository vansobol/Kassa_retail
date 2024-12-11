import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
import time
import logging

def test_correction(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 15)
    try:
        side_menu = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton")))
        side_menu.click()
    except StaleElementReferenceException:
        side_menu = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton")))
        side_menu.click()
    try:
        error = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1')))
        text = error.text
        logging.info(text)
    except TimeoutException:
        logging.info("Ошибок оплаты нет. Продолжаем выполнение теста.")

    correction = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Коррекция']")
    correction.click()
    time.sleep(1)
    correction_sale = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_name"])[9]')))
    correction_sale.click()

    add_receipt_items = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item')))
    add_receipt_items.click()
    time.sleep(2)
    menu_search = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search')))
    menu_search.click()
    search_input = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input.clear()
    search_input.send_keys("Доставка")

    try:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[1]")))
        select_item.click()
    except StaleElementReferenceException:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
        select_item.click()
    done = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done')))
    done.click()
    continue_button = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    continue_button.click()
    calendar_open = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_document_date')))
    calendar_open.click()
    button_ok = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'android:id/button1')))
    button_ok.click()
    number_doc = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Номер документа"]')))
    number_doc.send_keys("1")
    action_button = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/action_button')))
    action_button.click()
    without_change = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, ("//android.widget.Button[@text='Без сдачи']"))))
    without_change.click()
    sno = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system')))
    sno.click()
    sno_select = wait.until(
        EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    sno_select.click()
    button_pay = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay')
    button_pay.click()

