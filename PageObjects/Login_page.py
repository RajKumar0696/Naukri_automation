from selenium.webdriver.common.by import By


class Login_page:
    login_link_xpath = "//a[text()='Login']"
    email_id_text_xpath = "//div[@class='form-row']//input[@type='text']"
    password_text_xpath = "//div[@class='form-row']//input[@type='password']"
    login_button_xpath = "//button[text()='Login']"
    view_profile_link_xpath = "//div[@class='view-profile-wrapper']"
    full_name_xpath = "//div[@class='hdn'] //span[@class='fullname']"
    logout_menu_xpath = "//div[@class='nI-gNb-drawer__icon']"
    logout_link_xpath = "//a[@title='Logout']"
    edit_button_xpath = "//em[text()='editOneTheme']"
    name_field_xpath = "//input[@id='name']"
    save_button_css = "#saveBasicDetailsBtn"
    last_update_xpath = "//span[@class='typ-14Medium mod-date-val']"

    def __init__(self,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.XPATH, self.login_link_xpath).click()

    def enter_email_id(self,email_id):
        self.driver.find_element(By.XPATH, self.email_id_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_id_text_xpath).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_text_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def get_login_page_title(self):
        login_title = self.driver.title
        print(login_title)
        return login_title

    def click_view_profile(self):
        self.driver.find_element(By.XPATH, self.view_profile_link_xpath).click()

    def fetch_full_name(self):
        name = self.driver.find_element(By.XPATH, self.full_name_xpath)
        full_name = name.text
        return full_name


    def click_logout_menu(self):
        self.driver.find_element(By.XPATH, self.logout_menu_xpath).click()

    def click_edit_button(self):
        self.driver.find_element(By.XPATH, self.edit_button_xpath).click()

    def edit_values(self,name):
        self.driver.find_element(By.XPATH, self.name_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.name_field_xpath).send_keys(name)

    def clcik_save_button(self):
        # self.driver.execute_script("arguments[0].scrollIntoView();",self.save_button_css)
        self.driver.find_element(By.CSS_SELECTOR, self.save_button_css).click()

    def get_last_update(self):
        actual = self.driver.find_element(By.XPATH, self.last_update_xpath).text
        return actual



    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    def get_home_page_title(self):
        home_title = self.driver.title
        return home_title


