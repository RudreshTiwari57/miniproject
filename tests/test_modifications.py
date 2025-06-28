from pages.ui.login import Login
from utilities.global_utiles import *
import pytest

@log_function(logger)
@pytest.mark.parametrize("data",yaml_file_contents)
def test_modifiy_user_bio_on_naukri(data):
    login: Login = Login()
    driver = login.login(data['username'], data['password'],data['user_name_profile'])

