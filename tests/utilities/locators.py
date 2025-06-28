# ---------------------------------------- Login ---------------------------------------------------------
login_page_username_input_box   :str = "//input[contains(@placeholder,'Enter your active Email ID / Username')]"
login_page_password_input_box   :str = "//input[contains(@placeholder,'Enter your password')]"
login_page_login_button :str = "//button[starts-with(@class,'btn-primary') and contains(@class,'loginButton')]"

# ---------------------------------------- Home -----------------------------------------------------------------
home_page_login_button  :str = "//a[@id='login_Layer']"
home_page_user_verification: str = '//div[@title="usre_name_propfile"]'
home_page_user_profile_image: str = "//img[@class='nI-gNb-icon-img' and @alt='naukri user profile img']"
home_page_user_profile_verification: str = '//div[@class="nI-gNb-info__heading" and @title="RUDRESH TIWARI"]'
home_page_user_profile_view_update_link: str = '//a[@class="nI-gNb-info__sub-link" and contains(text(),"View & Update Profile")]'


# ---------------------------------------- user profile -----------------------------------------------------

user_profile_page_verification: str = '//span[@class="fullname"]'
user_profile_page_resume_heading: str = '//div[@class="widgetHead"]/span[text()="Resume headline"]/following-sibling::span'
user_profile_page_resume_heading_widget_verification: str = '//div[@class="widgetHead"]/span[text()="Resume headline"]'
user_profile_page_resume_heading_widget_inputbox: str = '//textarea[@id="resumeHeadlineTxt"]'
user_profile_page_resume_heading_widget_save: str = '//button[@class="btn-dark-ot" and@type="submit"]'
user_profile_page_resume_heading_text: str = '//div[@id="lazyResumeHead"]//div[@class="widgetCont"]/div[contains(@class,"typ-14Medium")]/div'