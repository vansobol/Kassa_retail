import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from driver_helper import WebDriverHelper
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
import logging
from pages.pay import PayPage
from pages.sale_screen import SaleScreen

def test_correction(driver_setup):
    driver, udid = driver_setup
    webdriver_helper = WebDriverHelper(driver)
    pay_page = PayPage(webdriver_helper)
    sale_screen = SaleScreen(driver)
    try:
        side_menu = webdriver_helper.wait_visible((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
        side_menu.click()
    except StaleElementReferenceException:
        side_menu = webdriver_helper.wait_visible((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
        side_menu.click()
    try:
        error = webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
        text = error.text
        logging.info(text)
    except TimeoutException:
        logging.info("Ошибок нет. Продолжаем выполнение теста.")

    correction = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Коррекция']")
    correction.click()
    time.sleep(1)
    sale_screen.close_banner()
    correction_sale = webdriver_helper.wait_visible((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_name"])[9]'))
    correction_sale.click()
    sale_screen.close_banner()
    add_receipt_items = webdriver_helper.wait_visible((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item'))
    add_receipt_items.click()
    time.sleep(2)
    menu_search = webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search'))
    menu_search.click()
    search_input = webdriver_helper.short_wait_present((AppiumBy.ID, 'android:id/search_src_text'))
    search_input.clear()
    search_input.send_keys("Доставка")

    try:
        select_item = webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[1]"))
        select_item.click()
    except StaleElementReferenceException:
        select_item = webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
        select_item.click()
    done = webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done'))
    done.click()
    continue_button = webdriver_helper.wait_visible((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue'))
    continue_button.click()
    calendar_open = webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_document_date'))
    calendar_open.click()
    button_ok = webdriver_helper.wait_visible((AppiumBy.ID, 'android:id/button1'))
    button_ok.click()
    number_doc = webdriver_helper.short_wait_present((AppiumBy.XPATH, '//android.widget.EditText[@text="Номер документа"]'))
    number_doc.send_keys("1")
    action_button = webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/action_button'))
    action_button.click()
    pay_page.cash_payment()

