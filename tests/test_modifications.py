from selenium.webdriver.remote.webelement import WebElement

from pages.ui.login import Login
from utilities.global_utiles import *
import pytest

@log_function(logger)
@pytest.mark.parametrize("data",yaml_file_contents)
def test_modifiy_user_bio_on_naukri(data)   -> None:
    login: Login = Login()
    driver : WebElement = login.login(data['username'], data['password'],data['user_name_profile'])

