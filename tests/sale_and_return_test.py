import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
import time
import re
import logging
from driver_helper import WebDriverHelper
from pages.search_goods import SearchGoods
from pages.loyality import LoyaltyPage
from pages.pay import PayPage


def test_sale_and_return(driver_setup):
    driver, udid = driver_setup
    webdriver_helper = WebDriverHelper(driver)
    search_goods = SearchGoods(webdriver_helper)
    loyalty = LoyaltyPage(webdriver_helper)
    pay_page = PayPage(webdriver_helper)
    search_goods.search_product("АГЕНТ")
    search_goods.search_features("ХАРАКТЕРИСТИКИ")
    loyalty.perform_loyalty_actions()
    total = webdriver_helper.wait_visible((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue'))
    match = re.search(r"Итог: (\d+)", total.text)
    result_expect = 175

    if match:
        result = int(match.group(1))  # Преобразовать строку "175" в число

        # Проверяем совпадение результата с ожидаемым
        if result == result_expect:
           logging.info(f"{result} = {result_expect} значение итога верное")
        else:
            logging.info(f"{result} != {result_expect} значение итога неверное")
    else:
        logging.info("Не удалось найти значение итога.")

    total.click()
    pay_page.non_cash_payment()

    try:
        side_menu = webdriver_helper.wait_visible((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
        side_menu.click()
    except StaleElementReferenceException:
        side_menu = webdriver_helper.wait_visible((AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"))
        side_menu.click()
    try:
        error = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1')))
        text = error.text
        logging.info(text)
    except TimeoutException:
        logging.info("Ошибок оплаты нет. Продолжаем выполнение теста.")

    sale_return = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Возврат прихода']")
    sale_return.click()
    search_goods.search_product("БАНКОВСКИЙ АГЕНТ")
    done = webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done'))
    done.click()
    time.sleep(1)
    total = webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_continue'))
    total.click()
    pay_page.cash_payment()



