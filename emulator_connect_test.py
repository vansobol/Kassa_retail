import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


def test_emulator(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 20)
    time.sleep(1)
    side_menu = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.view.ViewGroup/android.widget.ImageButton")))
    side_menu.click()
    time.sleep(1)
    driver.swipe(100, 2000, 100, 600, duration=1500)

    settings = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Настройки']")
    settings.click()

    kkt_settings = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.bifit.cashdesk.mobile:id/text_kkt_name')))
    kkt_settings.click()

    add_kkt = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_add')))
    add_kkt.click()

    button_next = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_next')))
    button_next.click()

    name_kkt = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout / android.widget.EditText")))
    name_kkt.send_keys('1')
    save = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_save')
    save.click()
    try:
        button_back = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton')))
        button_back.click()
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
    try:
        side_menu = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open')))
        side_menu.click()
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

    kassa = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_recycler_view"]/android.view.ViewGroup[1]')))
    kassa.click()
    kassa_sale = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.bifit.cashdesk.mobile:id/material_drawer_name" and @text="Приход"]' )))
    kassa_sale.click()