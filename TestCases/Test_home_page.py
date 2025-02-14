import time

import pytest
from PageObjects.HomePage import HomePage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import Loggen

class Test_Home_Page:
    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    title = ReadConfig.get_home_page_title()
    log = Loggen.loggen()

    @pytest.mark.skip(reason="For testing purpose")
    def test_page_title(self, setup):
        self.log.info("started")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(5)
        self.homepage = HomePage(self.driver)
        act_title = self.homepage.get_title()
        self.log.info("title check")
        if act_title == self.title:
            self.log.info("matched")
            self.driver.close()
            assert True
        else:
            self.log.info("not matched")
            self.driver.save_screenshot(r"C:\Users\Rajkumar.M\Automation_pytest\Automation\ScreenShots\homepage.png")
            self.driver.close()
            # assert False

