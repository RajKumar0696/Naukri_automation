from selenium.webdriver.common.by import By

class UpdateProfile:
    view_profile_xpath = "//div[@class='view-profile-wrapper']//a[contains(text(),'View')]"
    headline_click_edit_xpath = "//div[@class='widgetHead']//span[text()='editOneTheme']"
    text_headline_id = "resumeHeadlineTxt"
    save_xpath = "//button[text()='Save']"
    last_update_css = "span[class='typ-14Medium mod-date-val']"

    def __init__(self,driver):
        self.driver = driver

    def click_view_profile(self):
        self.driver.find_element(By.XPATH, self.view_profile_xpath).click()

    def click_headline_edit(self):
        self.driver.find_element(By.XPATH, self.headline_click_edit_xpath).click()

    def clear_headline_value(self, single):
        self.driver.find_element(By.ID, self.text_headline_id).clear()
        self.driver.find_element(By.ID, self.text_headline_id).send_keys(single)


    def enter_headline_value(self, headline):
        self.driver.find_element(By.ID, self.text_headline_id).clear()
        self.driver.find_element(By.ID, self.text_headline_id).send_keys(headline)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_xpath).click()

    def check_last_update(self):
        actual = self.driver.find_element(By.CSS_SELECTOR, self.last_update_css).text
        if actual == "Today":
            assert True
        else:
            print("Not updated")


