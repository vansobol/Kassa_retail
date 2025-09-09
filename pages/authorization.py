from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
import time
import logging
from driver_helper import WebDriverHelper
from appium.webdriver.common.touch_action import TouchAction

class Authorization:
    def __init__(self, driver):
        self.driver = driver
        self.helper = WebDriverHelper(driver)
    def allow_permissions(self):

        try:
            allow_button1 = self.helper.short_wait_present((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'))
            allow_button1.click()
            allow_button2 =self.helper.short_wait_present((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'))
            allow_button2.click()
        except TimeoutException:
            logging.info("Кнопка permission_allow_foreground_only_button не найдена. Продолжаем выполнение теста.")
        try:
            allow_button_alt = self.helper.short_wait_present((AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button'))
            allow_button_alt.click()
            allow_button_alt = self.helper.short_wait_present((AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button'))
            allow_button_alt.click()

        except TimeoutException:
            logging.info("Кнопка permission_allow_button не найдена. Продолжаем выполнение теста.")
        try:
            allow_button_alt2 = self.helper.short_wait_present((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'))
            allow_button_alt2.click()
        except  TimeoutException:
            logging.info("Кнопка permission_allow_button2 не найдена. Продолжаем выполнение теста.")

    def login(self, username, password):
        login_field = self.helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/phone_input'))
        login_field.send_keys(username)

        password_field = self.driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/password_input')
        password_field.send_keys(password)

        login_button = self.driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_login')
        login_button.click()

    def click_access_code(self):
        for _ in range(2):
            button_1 = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_1'))
            button_1.click()

            button_2 = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_2'))
            button_2.click()

            button_3 = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_3'))
            button_3.click()

            button_4 = self.helper.short_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_4'))
            button_4.click()

    def select_organization_and_object(self):
        try:
            first_organization = self.helper.wait_present((AppiumBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]"))
            start_time = time.time()
            first_organization.click()
        except TimeoutException:
            logging.info("Выбор организаций отсутствует.Продолжаем выполнение теста")
            pass

        try:
            first_object = self.helper.short_wait_present((AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.bifit.cashdesk.mobile:id/recycler"]/android.widget.RelativeLayout[1]'))
            first_object.click()
        except TimeoutException:
            print("Выбор торговых объектов отсутствует.Продолжаем выполнение теста")
            pass
        timeout_duration = self.helper.short_wait._timeout
        try:
            skip_1 = self.helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_skip'))
            skip_1.click()
            skip_2 = self.helper.short_wait_present((AppiumBy.XPATH, "//android.widget.Button[2]"))
            if skip_2.is_displayed() and skip_2.is_enabled():
                skip_2.click()
            end_time = time.time()
            logging.info(f"Время загрузки торгового объекта: {end_time - start_time:.0f} секунд")
            logging.info("Экран подключения эмулятора и терминала присутствуют")
        except TimeoutException:
            logging.info("Экраны подключения эмулятора и терминала отсутствуют")
            end_time = time.time()
            elapsed_time = end_time - start_time - timeout_duration  # Вычитаем время ожидания таймаута
            logging.info(f"Время загрузки торгового объекта (с учетом таймаута): {elapsed_time:.0f} секунд")

    # def swipe_up(self, duration=800):
    #     w, h = self.driver.get_window_size().values()
    #     TouchAction(self.driver).press(x=w // 2, y=int(h * 0.8)) \
    #         .wait(ms=duration) \
    #         .move_to(x=w // 2, y=int(h * 0.2)) \
    #         .release() \
    #         .perform()
    #
    def close_banner(self):
        try:
            close_btn = self.helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/closeBtn'))
            close_btn.click()
        except TimeoutException:
            logging.info("Уведомлений не обнаружено")


