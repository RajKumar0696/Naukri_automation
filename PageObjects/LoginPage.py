from selenium.webdriver.common.by import By

class Login:
    login_link_id = "login_Layer"
    email_place_xpath = "//input[@placeholder='Enter your active Email ID / Username']"
    password_place_xpath = "//input[@placeholder='Enter your password']"
    login_button_xpath = "//button[text()='Login']"

    def __init__(self,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.ID, self.login_link_id).click()

    def enter_email(self, email_id):
        self.driver.find_element(By.XPATH, self.email_place_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_place_xpath).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_place_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_place_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

