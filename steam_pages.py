from base_page import BasePage
from selenium.webdriver.common.by import By


class SteamSearchLocators:
    SEARCH_FIELD_LOCATOR = (By.XPATH, "//input[@id='store_nav_search_term']")
    SEARCH_BUTTON_LOCATOR = (By.XPATH,"//*[@id='store_search_link']/img")
    SORT_BUTTON_LOCATOR = (By.XPATH, "//*[@id='sort_by_trigger']")
    DESCENDING_ORDER_OPTION_LOCATOR = (By.XPATH, "//*[@id='Price_DESC']")


class SteamMain(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SteamSearchLocators.SEARCH_FIELD_LOCATOR)
        search_field.send_keys(word)
        return search_field

    def click_on_search_button(self):
        return self.find_element(SteamSearchLocators.SEARCH_BUTTON_LOCATOR, time=3).click()

    def sort_in_descending_order(self):
        sort_button = self.find_element(SteamSearchLocators.SORT_BUTTON_LOCATOR)
        sort_button.click()
        descending_order = self.find_element(SteamSearchLocators.DESCENDING_ORDER_OPTION_LOCATOR)
        descending_order.click()
