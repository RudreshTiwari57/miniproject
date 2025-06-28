import time

from selenium.webdriver.remote.webelement import WebElement

from pages.ui.home import Home
from pages.ui.login import Login
from pages.ui.user_profile import User_Profile
from utilities.global_utiles import *
import pytest

@log_function(logger)
@pytest.mark.parametrize("data",yaml_file_contents)
def test_modifiy_user_bio_on_naukri(data)   -> None:
    login: Login = Login()
    driver : WebElement = login.login(data['username'], data['password'],data['user_name_profile'])
    home: Home = Home(driver)
    home.click_on_user_profile()
    user_profile:   User_Profile = User_Profile(driver)
    user_profile.modifiy_user_resume_headline(data["user_resume_headline"])

