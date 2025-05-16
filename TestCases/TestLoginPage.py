from Utilities.Reagconfig import ReadConfig
from PageObjects.LoginPage import Login

class Test_login_page:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    title = ReadConfig.get_page_title()


    def test_login(self, setup):
        self.driver = setup

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
        self.login.click_login_link()
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login_button()
        actual_title = self.driver.title
        self.driver.close()

        assert actual_title == self.title, f"Expected title '{self.title}', but got '{actual_title}'"





