from selenium.webdriver.remote.webelement import WebElement

from utilities.locators import *
from utilities.global_utiles import *
from playwright.sync_api import sync_playwright, Page


class Base:
    @log_function(logger)
    def launch_browser(self)    -> WebElement:
        chrome = sync_playwright().start()
        browser = chrome.chromium.launch(headless=False)
        driver = browser.new_page()
        driver.goto("https://naukri.com")
        return driver