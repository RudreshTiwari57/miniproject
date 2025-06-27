from utilities.locators import *
from utilities.global_utiles import *
from utilities.base import Base
from playwright.sync_api import Page
class Login:
    @log_function(logger)
    def login(self,
              username: str,
              password: str,
              user_profile_name) -> Page:
        driver: Page = Base().launch_browser()
        driver.locator(home_page_login_button).click()
        driver.locator(login_page_username_input_box).click()
        driver.locator(login_page_username_input_box).type(username)
        driver.locator(login_page_password_input_box).click()
        driver.locator(login_page_password_input_box).type(password)
        driver.locator(login_page_login_button).click()
        driver.wait_for_selector(home_page_user_verification.replace("usre_name_propfile", user_profile_name))
        assert "Home" in driver.title(), "cannot login to the naukri app"
        return driver