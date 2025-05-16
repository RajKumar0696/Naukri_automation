import time

from PageObjects.UpdateProfile import UpdateProfile
from PageObjects.LoginPage import Login
from Utilities.Reagconfig import ReadConfig

class TestLastUpdate:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    headline = ReadConfig.get_headline()

    def test_last_update(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
        self.login.click_login_link()
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login_button()
        try:
            self.update = UpdateProfile(self.driver)
            self.update.click_view_profile()
            self.update.click_headline_edit()
            self.update.clear_headline_value("I am updating my profile through automation")
            self.update.click_save()
            time.sleep(3)
            self.driver.back()
            self.update.click_view_profile()
            self.update.click_headline_edit()
            self.update.enter_headline_value(self.headline)
            self.update.click_save()
            self.update.check_last_update()
        except:
            print("Process not completed please check logs")
        finally:
            self.driver.close()

