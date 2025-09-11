import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from driver_helper import WebDriverHelper
import logging



class AddMarkGood:
    def __init__(self, webdriver_helper):
        self.webdriver_helper = webdriver_helper
        self.driver = webdriver_helper.driver

    def close_search(self):
        add_receipt_items = self.webdriver_helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item'))
        add_receipt_items.click()
        try:
            search_close =self.webdriver_helper.short_wait_present((AppiumBy.ID, 'android:id/search_close_btn'))
            search_close.click()
            search_close2 = self.webdriver_helper.short_wait_present((AppiumBy.ID, 'android:id/search_close_btn'))
            search_close2.click()
        except TimeoutException:
            logging.info("Элемент 'search_close'  не найден, продолжаем выполнение теста.")

    def add_mark(self,mark):
        select_item = self.webdriver_helper.wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(16)'))
        select_item.click()
        ActionChains(self.driver).send_keys(mark).send_keys(Keys.ENTER).perform()

    def mark_check(self):
        # Проверка и закрытие всплывающего окна после клика на кнопку total
        try:
            # Проверка на наличие ошибки
            error = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/textView1'))
            text = error.text
            logging.info(f"Сообщение об ошибке: {text}")

            # Закрытие всплывающего сообщения
            close_button = self.webdriver_helper.middle_wait_clickable((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/closeBtn'))
            close_button.click()
            logging.info("Закрыто сообщение об ошибке ЛМ ЧЗ")
        except (TimeoutException, NoSuchElementException):
            logging.info("Сообщение об ошибке ЛМ ЧЗ не появилось")

        try:
            # Кнопка "Продолжить"
            oism_button = self.webdriver_helper.middle_wait_present((AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.bifit.cashdesk.mobile:id/button_continue" and @text="Далее"]'))
            oism_button.click()
            logging.info("Кнопка Продолжить нажата")

        except (StaleElementReferenceException, TimeoutException, NoSuchElementException):
            # Пробуем найти "Удалить невалидные"
            try:
                oism_button2 = self.webdriver_helper.middle_wait_present((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.bifit.cashdesk.mobile:id/button_continue" and @text="Удалить невалидные"]'))
                oism_button2.click()
                logging.info("Есть невалидные марки,нажата кнопка Удалить невалидные")
                time.sleep(1)

                input_field = self.webdriver_helper.middle_wait_present((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/edit_text_mark")'))
                mark = "04601653035829H;dV)bFACVUdGVz"
                input_field.send_keys(mark)
                ActionChains(self.driver).send_keys(mark).send_keys(Keys.ENTER).perform()


                try:
                    # Попытка удалить марку
                    delete_mark = self.webdriver_helper.wait_clickable((AppiumBy.ID,"com.bifit.cashdesk.mobile:id/button_delete" ))
                    delete_mark.click()
                    logging.info("Кнопка удаления марки нажата")
                except (TimeoutException, NoSuchElementException):
                    logging.info("Удаление невалидных данных: кнопка удаления неактивна")

            except (StaleElementReferenceException, TimeoutException, NoSuchElementException):
                # Проверяем, перешли ли сразу на страницу оплаты
                try:
                    self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//android.widget.Button[@text='Без сдачи']"))
                    logging.info("Окна проверки ЧЗ отсутствует")
                except TimeoutException:
                    logging.warning("Не удалось определить состояние")