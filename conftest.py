import pytest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException, TimeoutException
from appium.options.android import UiAutomator2Options
import subprocess
import logging

appActivity = {

}

def get_connected_devices():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    devices = [line.split()[0] for line in output.strip().splitlines() if 'device' in line and 'List' not in line]
    return devices


@pytest.fixture(scope='function', params=get_connected_devices())
def driver_setup(request):
    udid = request.param
    options = UiAutomator2Options()
    options.platformName = 'android'
    options.udid = udid
    options.automationName = 'uiautomator2'
    options.appPackage = 'com.bifit.cashdesk.mobile'
    options.appActivity = 'com.bifit.cashdesk.mobile.StartActivity'
    options.newCommandTimeout = 10
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    yield driver, udid
    driver.quit()

def pytest_configure():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),  # Вывод в консоль
            logging.FileHandler("test_logs.log", mode='a',encoding='utf-8')  # Запись в файл
        ]
    )

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # Этот фикстур выполняется для всех тестов и настраивает логирование
    logging.info("Тесты запускаются")
    yield
    logging.info("Тесты завершены")


# @pytest.fixture()
# def driver_neva():
#     options = UiAutomator2Options()
#     options.platformName = 'android',
#     options.udid = '1043b195'
#     options.automationName = 'uiautomator2',
#     options.appPackage = 'com.bifit.cashdesk.mobile',
#     options.appActivity = 'com.bifit.cashdesk.mobile.StartActivity',
#     options.autoGrantPermissions = True,
#     options.noReset = True,
#     options.newCommandTimeout = 10,
#     driver = webdriver.Remote('http://localhost:4723', options=options)
#     yield driver
#     driver.quit()
# @pytest.fixture()
# def driver_mspos():
#     options = UiAutomator2Options()
#     options.platformName = 'android',
#     options.udid = '1043b195'
#     options.automationName = 'uiautomator2',
#     options.appPackage = 'com.bifit.cashdesk.mobile',
#     options.appActivity = 'com.bifit.cashdesk.mobile.StartActivity',
#     options.autoGrantPermissions = True,
#     options.noReset = True,
#     options.newCommandTimeout = 10,
#     driver = webdriver.Remote('http://localhost:4723', options=options)
#     yield driver
#     driver.quit()

@pytest.fixture()
def setup_before_test(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 15)

    try:
        kassa = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Касса')
        kassa.click()
    except Exception as e:
        print("An error occurred:", str(e))

    account = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.LinearLayout')))
    account.click()

    # Проверяем наличие кнопок
    try:
        button_1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_1')))
        button_1.click()

        button_2 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_2')))
        button_2.click()

        button_3 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_3')))
        button_3.click()

        button_4 = wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_4')))
        button_4.click()

    except TimeoutException:
        print("Код кассира не установлен,переходим к выбору организации")

    # Переход к организации
    start_time = time.time()
    first_organization = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ListView/android.widget.LinearLayout[1]')))
    first_organization.click()

    # Выбор объекта
    first_object = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]')))
    loading_organization_time = time.time()
    first_object.click()

    time.sleep(6)

    # Прокрутка экрана
    try:
        driver.swipe(100, 2000, 100, 600, duration=1500)
    except NoSuchElementException:
        pass
    except InvalidElementStateException:
        pass

    loading_trade_objects_time = time.time()

    # Вычисление времени загрузки
    time_for_loading_organization = loading_organization_time - start_time
    time_for_trade_objects = loading_trade_objects_time - loading_organization_time
    print(f"Время загрузки организаций: {time_for_loading_organization} секунд")
    print(f"Время загрузки торговых объектов: {time_for_trade_objects} секунд")


