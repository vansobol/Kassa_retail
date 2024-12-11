import logging
from appium.webdriver.common.appiumby import AppiumBy
import time
from driver_helper import WebDriverHelper
from selenium.common.exceptions import TimeoutException
from pages.authorization import Authorization


def test_reauthorization(driver_setup):
    driver, udid = driver_setup
    webdriver_helper = WebDriverHelper(driver)
    side_menu = webdriver_helper.short_wait_present((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
    side_menu.click()
    time.sleep(1)
    webdriver_helper.driver.swipe(100, 2000, 100, 600, duration=1500)
    exit = webdriver_helper.short_wait_present((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(16)'))
    exit.click()
    exit_done = webdriver_helper.wait_visible((AppiumBy.ID,'com.bifit.cashdesk.mobile:id/button_yes'))
    exit_done.click()
    try:
        # Клик по элементу аккаунта
        account = webdriver_helper.wait_present(
            (AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.LinearLayout'))
        account.click()

        # Проверяем наличие кнопок и кликаем по ним
        button_ids = [
            'com.bifit.cashdesk.mobile:id/button_1',
            'com.bifit.cashdesk.mobile:id/button_2',
            'com.bifit.cashdesk.mobile:id/button_3',
            'com.bifit.cashdesk.mobile:id/button_4',
        ]

        for button_id in button_ids:
            button = webdriver_helper.short_wait_present((AppiumBy.ID, button_id))
            button.click()
        logging.info("Код кассира введен")

    except TimeoutException:
        logging.info("Код кассира не установлен, переходим к выбору организации")


    authorization = Authorization(driver)
    authorization.select_organization_and_object()
