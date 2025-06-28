from selenium.webdriver.remote.webelement import WebElement
from utilities.locators import *
from utilities.global_utiles import *
from utilities.base import Base
from playwright.sync_api import Page

class Home:
    def __init__(self,
                 driver : Page)   -> Page:

        self.driver : Page = driver


    def click_on_user_profile(self) -> None:

        self.driver.locator(home_page_user_profile_image).click()
        self.driver.wait_for_selector(home_page_user_profile_verification,state='visible')
        self.driver.locator(home_page_user_profile_view_update_link).click()


