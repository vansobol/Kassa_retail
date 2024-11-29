import pytest
from pytest_lazyfixture import lazy_fixture
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
import time
import subprocess
from appium.webdriver.common.touch_action import TouchAction


def test_authorization_android(driver_setup):

    driver,udid = driver_setup
    wait = WebDriverWait(driver, 20)
    subprocess.run(['adb','-s',udid, 'shell', 'pm', 'clear', 'com.bifit.cashdesk.mobile'])
    time.sleep(2)
    subprocess.run(['adb', '-s', udid, 'shell', 'am', 'start','com.bifit.cashdesk.mobile/com.bifit.cashdesk.mobile.StartActivity'])

    time.sleep(1)

    try:
        allow_button1 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')))
        allow_button1.click()
        allow_button2 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
        allow_button2.click()
    except TimeoutException:
        print("Кнопка permission_allow_foreground_only_button не найдена. Продолжаем выполнение теста.")
    try:
        allow_button_alt = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        allow_button_alt.click()
        allow_button_alt = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        allow_button_alt.click()

    except TimeoutException:
        print("Кнопка permission_allow_button не найдена. Продолжаем выполнение теста.")


    login_field = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/phone_input')))
    login_field.send_keys('demo@demo')

    password_field = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/password_input')
    password_field.send_keys('1234qwer')

    login_button = driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_login')

    login_button.click()

    for _ in range(2):
        button_1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_1')))
        button_1.click()

        button_2 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_2')))
        button_2.click()

        button_3 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_3')))
        button_3.click()

        button_4 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_4')))
        button_4.click()
    try:
       first_organization = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")))
       first_organization.click()
    except TimeoutException:
       print("Выбор организаций отсутствует.Продолжаем выполнение теста")
       pass
    try:
        first_object = WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.XPATH,  '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.bifit.cashdesk.mobile:id/recycler"]/android.widget.RelativeLayout[1]')))
        first_object.click()
    except TimeoutException:
       print("Выбор торговых объектов отсутствует.Продолжаем выполнение теста")
       pass

    try:
        skip_1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_skip')))
        skip_1.click()
        print("Экран подключения эмулятора")
    except TimeoutException:
        print("Экран подключения эмулятора  отсутствует")
        # Завершение теста успешно, если первый элемент не найден
        pytest.exit("Тест завершен успешно")

    try:
        skip_2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[2]")))
        if skip_2.is_displayed() and skip_2.is_enabled():
            skip_2.click()
    except TimeoutException:
        print("Экран подключения терминала  отсутствует")
