import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    browser = webdriver.Chrome()

    return browser
