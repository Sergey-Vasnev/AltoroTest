from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage: #create class for a base page we are going to work with
    def __init__(self,driver):
        self.driver=driver
        self.base_url = "http://testfire.net/feedback.jsp"

    def find_element(self, locator, time = 10): #creates special element finding function
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}") #with imported webdriverwait function waits till it finds locator element
    def go_to_site(self):
        return self.driver.get(self.base_url) #returns the base_url value

    def return_current_url(self,driver): #function returns current url
        check_url=driver.current_url #with driver current_url function saves value in check_url variable
        return check_url
