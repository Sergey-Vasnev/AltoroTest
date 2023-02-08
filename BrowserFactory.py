import pytest
from selenium import webdriver
import Singleton

class Driver():
    @staticmethod
    def chooseDriver(browser_name):
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            return webdriver.Chrome()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
            return browser
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")



