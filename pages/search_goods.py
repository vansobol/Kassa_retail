from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class SearchGoods:
    def __init__(self, webdriver_helper):
        self.webdriver_helper = webdriver_helper

    def search_product(self, product_name):
        """
        Поиск и выбор товара по имени.
        :param product_name: Название товара для поиска.
        """
        add_receipt_items = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/button_add_receipt_item'))
        add_receipt_items.click()
        menu_search = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search'))
        menu_search.click()

        search_input = self.webdriver_helper.wait_present((AppiumBy.ID, 'android:id/search_src_text'))
        search_input.clear()
        search_input.send_keys(product_name)

        try:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[2]"))
            select_item.click()
        except StaleElementReferenceException:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
            select_item.click()
        except TimeoutException:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
            select_item.click()

    def search_features(self, feature_name):
        """
        Поиск и выбор характеристик товара по имени.
        :param feature_name: Название характеристики для поиска.
        """
        menu_search = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/menu_item_search'))
        menu_search.click()

        search_input = self.webdriver_helper.wait_present((AppiumBy.ID, 'android:id/search_src_text'))
        search_input.clear()
        search_input.send_keys(feature_name)

        try:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.bifit.cashdesk.mobile:id/recycler']/android.view.ViewGroup[2]"))
            select_item.click()
        except StaleElementReferenceException:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
            select_item.click()
        except TimeoutException:
            select_item = self.webdriver_helper.short_wait_present((AppiumBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
            select_item.click()

        feature = self.webdriver_helper.wait_visible((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.bifit.cashdesk.mobile:id/item_nomenclature_feature").instance(1)'))
        feature.click()

        done = self.webdriver_helper.wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile:id/fab_done'))
        done.click()
