import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.extensions.android.nativekey import AndroidKey


def test_sale_and_return(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 15)
    add_receipt_items = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item')))
    add_receipt_items.click()
    time.sleep(2)
    menu_search = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search')))
    menu_search.click()

    search_input1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input1.clear()
    search_input1.send_keys("АГЕНТ")
    try:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[2]")))
        select_item.click()
    except StaleElementReferenceException:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
        select_item.click()
    menu_search = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search')))
    menu_search.click()

    search_input2 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input2.clear()
    search_input2.send_keys("ХАРАКТЕРИСТИКИ")

    try:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[2]")))
        select_item.click()
    except StaleElementReferenceException:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
        select_item.click()
    feature_1 = wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/item_nomenclature_feature").instance(1)')))
    feature_1.click()

    done = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done')))
    done.click()
    loyalty_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/image_receipt_discount')))
    loyalty_button.click()
    add_loyalty_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add')))
    add_loyalty_button.click()
    input_number = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/loyaltyInput")')))
    input_number.send_keys("22222")
    add_button = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/button_add").instance(1)')))
    add_button.click()
    add_loyalty_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add')))
    add_loyalty_button.click()
    input_number2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/loyaltyInput")')))
    input_number2.send_keys("44444")
    add_button = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/button_add").instance(1)')))
    add_button.click()
    input_points = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Списать баллы")')))
    input_points.click()
    driver.press_keycode(12)
    driver.press_keycode(4)
    save_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    save_button.click()
    total = wait.until(EC.visibility_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    match = re.search(r"Итог: (\d+)", total.text)
    result_expect = 175

    if match:
        result = int(match.group(1))  # Преобразовать строку "175" в число

        # Проверяем совпадение результата с ожидаемым
        if result == result_expect:
            print(f"{result} = {result_expect} значение итога верное")
        else:
            print(f"{result} != {result_expect} значение итога неверное")
    else:
        print("Не удалось найти значение итога.")

    total.click()
    try:
        non_cash = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')))
        non_cash.click()
    except NoSuchElementException:
        error = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1')))
        text = error.text
        print(text)
    except TimeoutException:
        error = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1')))
        text = error.text
        print(text)
    except Exception:
        print('Непредвиденная ошибка')
    sno = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system')))
    sno.click()
    sno_select = wait.until(
        EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    sno_select.click()
    button_pay = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay')))
    button_pay.click()

    try:
        side_menu = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton")))
        side_menu.click()
    except StaleElementReferenceException:
        side_menu = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton")))
        side_menu.click()
    try:
        error = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1')))
        text = error.text
        print(text)
    except TimeoutException:
        print("Ошибок оплаты нет. Продолжаем выполнение теста.")

    sale_return = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Возврат прихода']")
    sale_return.click()
    add_receipt_items = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item')))
    add_receipt_items.click()
    menu_search = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search')))
    menu_search.click()

    search_input1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/search_src_text')))
    search_input1.clear()
    search_input1.send_keys("БАНКОВСКИЙ АГЕНТ")
    try:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[1]")))
        select_item.click()
    except StaleElementReferenceException:
        select_item = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
        select_item.click()

    done = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done')))
    done.click()
    time.sleep(1)
    total = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue')))
    total.click()
    without_change = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, ("//android.widget.Button[@text='Без сдачи']"))))
    without_change.click()
    sno = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/text_input_tax_system')))
    sno.click()
    sno_select = wait.until(
        EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    sno_select.click()
    driver.implicitly_wait(10)
    button_pay = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_pay')
    button_pay.click()




