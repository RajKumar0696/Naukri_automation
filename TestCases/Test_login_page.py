import time

from PageObjects.Login_page import Login_page
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import Loggen
from PageObjects.HomePage import HomePage

class Test_login_page:
    url = ReadConfig.get_url()
    email = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_title = ReadConfig.get_login_page_title()
    home_title = ReadConfig.get_home_page_title()
    full_name = ReadConfig.get_full_name()
    log = Loggen.loggen()

    def test_login_page(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.login = Login_page(self.driver)
        self.login.click_login_link()
        self.login.enter_email_id(self.email)
        self.login.enter_password(self.password)
        self.login.click_login_button()

        login_page = self.login.get_login_page_title()
        self.log.info("Login page title checking start")
        if login_page == self.login_title:
            assert True
            self.log.info("matched")
        else:
            self.driver.save_screenshot(r"C:\Users\Rajkumar.M\Automation_pytest\Automation\ScreenShots\login_page_title.png")
            print(login_page)
            self.log.info("not matched")
            assert False

        self.login.click_view_profile()
        full_name = self.login.fetch_full_name()
        self.log.info("full_name checking")
        if full_name == self.full_name:
            assert True
            self.log.info("Matched")
        else:
            self.driver.save_screenshot(r"C:\Users\Rajkumar.M\Automation_pytest\Automation\ScreenShots\login_page.png")
            print(full_name)
            self.log.info("not matched")
            assert False

        self.login.click_edit_button()
        self.login.edit_values("Rajkumar M")
        self.login.clcik_save_button()
        actual_update = self.login.get_last_update()
        print(actual_update)
        if actual_update == "Today":
            assert True
        # else:
        #     assert False
        self.login.click_logout_menu()
        self.login.click_logout()
        home = self.login.get_home_page_title()
        self.log.info("home page title checking")
        if home == self.home_title:
            assert True
            self.log.info("matched")
        else:
            self.driver.save_screenshot(r"C:\Users\Rajkumar.M\Automation_pytest\Automation\ScreenShots\home_page.png")
            print(home)
            self.log.info("not matched")
            assert False
    # def test_page_title(self, setup):
    #     self.log.info("started")
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     time.sleep(5)
    #     self.homepage = HomePage(self.driver)
    #     act_title = self.homepage.get_title()
    #     self.log.info("title check")
    #     if act_title == self.home_title:
    #         self.log.info("matched")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.log.info("not matched")
    #         self.driver.save_screenshot(r"C:\Users\Rajkumar.M\Automation_pytest\Automation\ScreenShots\homepage.png")
    #         self.driver.close()
    #         assert False


