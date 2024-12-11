import time
import subprocess
import pytest
from pages.authorization import Authorization

def test_authorization_android(driver_setup):

    driver,udid = driver_setup
    subprocess.run(['adb','-s',udid, 'shell', 'pm', 'clear', 'com.bifit.cashdesk.mobile'])
    time.sleep(2)
    subprocess.run(['adb', '-s', udid, 'shell', 'am', 'start','com.bifit.cashdesk.mobile/com.bifit.cashdesk.mobile.StartActivity'])
    time.sleep(1)
    auth = Authorization(driver)
    auth.allow_permissions()
    auth.login(username='demo@demo', password='1234qwer')
    auth.click_access_code()
    auth.select_organization_and_object()