import pytest
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import qrcode
import base64
import os

def test_markirovka(driver_setup):
    driver, udid = driver_setup
    wait = WebDriverWait(driver, 15)

    mark = "04601653035829H;dV)bFACVUdGVz"


    ActionChains(driver).send_keys(mark).send_keys(Keys.ENTER).perform()

    # mark = "0000004621065422dBtACAAPidGVz"
    #
    #
    #
    #
    #
    # # Подготовка команды для ADB
    # input_command = f'adb shell input text "{mark}"'
    #
    # # Отправляем команду
    # os.system(input_command)
    #
    # # Нажимаем Enter после передачи строки
    # os.system("adb shell input keyevent 66")