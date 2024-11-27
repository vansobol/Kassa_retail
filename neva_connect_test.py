import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time

@pytest.mark.parametrize("driver_setup", ["1043b195"], indirect=True)
def test_neva(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 20)

    side_menu = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.view.ViewGroup/android.widget.ImageButton")))
    side_menu.click()
    time.sleep(2)
    driver.swipe(280, 850, 275, 450, duration=2000)

    settings = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Настройки']")
    settings.click()

    kkt_settings = wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.bifit.cashdesk.mobile:id/text_kkt_name')))
    kkt_settings.click()

    add_kkt = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_add')))
    add_kkt.click()

    select_vendor = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')))
    select_vendor.click()

    select_armax = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.LinearLayout[13]/android.widget.RelativeLayout/android.widget.TextView')))
    select_armax.click()

    button_next = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_next')))
    button_next.click()

    save = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_save')))
    save.click()
    try:
        button_back = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageButton')))
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