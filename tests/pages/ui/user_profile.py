import time

from selenium.webdriver.remote.webelement import WebElement
from utilities.locators import *
from utilities.global_utiles import *
from utilities.base import Base
from playwright.sync_api import Page



class User_Profile:
    def __init__(self,
                 driver : Page)   -> Page:

        self.driver : Page = driver

    def modifiy_user_resume_headline(self,
                                     resume_headline: str) -> None:

        self.driver.wait_for_selector(user_profile_page_verification,state="visible")
        self.driver.locator(user_profile_page_resume_heading).click()
        self.driver.wait_for_selector(user_profile_page_resume_heading_widget_verification,state='visible')
        self.driver.locator(user_profile_page_resume_heading_widget_inputbox).click()
        self.driver.locator(user_profile_page_resume_heading_widget_inputbox).clear()
        self.driver.locator(user_profile_page_resume_heading_widget_inputbox).fill(resume_headline)
        self.driver.locator(user_profile_page_resume_heading_widget_save).click()
        submitted_text : str = self.driver.locator(user_profile_page_resume_heading_text).text_content()
        assert submitted_text == resume_headline ,"profile updation was failed"
