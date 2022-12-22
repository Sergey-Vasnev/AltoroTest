# AltoroTest
Automated testing of Feedback form from Altoro Mutual

This program automates 2 tests for Feedback form on Altoro Mutual website (*http://testfire.net/feedback.jsp*)

1. [How to use the program and run tests](#how-to-use-the-program-and-run-tests)
2. [How does it works?](#how-does-it-works)

## How to use the program and run tests

I'm going to use selenium and pytest libraries for this program. You could install them via terminal
```
pip install pytest
pip install selenium
```

or PyCharm Python Packages

When all libraries were installed, you should write the following command into your terminal
```
pytest start.py
```
or
```
pytest -v start.py
```
to see more information about tests

This program runs 2 tests. The first one goes to feedback form, fills out only Your Name field, submits data and checks if we stayed on the same page or not. As the result this test is considered as failed due to websites logic which does not stops user from sending invalid data.
The second test tries to find the potential for XSS vulnerability. The program fills out Your Name filed with simple JavaScript command calling for an alert messege and submit data to the server. As the result our program catches the alert messege and is marked as 'passed'.

![Alt-текст](https://github.com/Sergey-Vasnev/AltoroTest/blob/main/result.png)

_____

## How does it works?

Firstly, we have pytest reserved conftest.py file for fixtures where we are going to implement initialization for WebDriver. 

```pytnon
import pytest
from selenium import webdriver

@pytest.fixture(scope="session") #creating fixture
def browser():
    driver = webdriver.Firefox() #sets Firefox as default webdriver
    yield driver
    driver.quit()
```

In the BaseApp.py file we create BasePage class which defines the basic working methods for webdriver. In our case there will be 3 functions: find_element, return_current_url and go_to_site

```pytnon
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
```

In the PageObject.py file we implement functions that are going to imitate user's actions during the tests themselves in the Feedback class. searchLocators class contains the locators, that are going to be used by our Feedback functions
```pytnon
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class searchLocators:
    SEARCH_FIELD_YOUR_NAME = (By.NAME, "name") #creates locator for Your Name field
    SEARCH_FIELD_YOUR_EMAIL = (By.NAME, "email_addr") #creates locator for Your Email Address field
    SEARCH_SUBJECT = (By.NAME, "subject") #creates locator for Subject field
    SEARCH_COMMENTS = (By.NAME, "comments") #creates locator for Question/Comment field
    SUBMIT_BUTTON = (By.NAME, "submit") #creates locator for 



class Feedback(BasePage):
    def enter_name(self,name): #find Your Name field, clicks on it and types data in it
        name_field = self.find_element(searchLocators.SEARCH_FIELD_YOUR_NAME)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def enter_email(self,email):#find Your Email Address field, clicks on it and types data in it
        enter_email = self.find_element(searchLocators.SEARCH_FIELD_YOUR_EMAIL)
        enter_email.click()
        enter_email.send_keys(email)
        return enter_email

    def enter_subject(self,subject): #finds Subject field, clicks on it and types data in it
        enter_subject = self.find_element(searchLocators.SEARCH_SUBJECT) #
        enter_subject.click()
        enter_subject.send_keys(subject)
        return enter_subject

    def enter_comments(self,comments): #finds Question/Comment field, clicks on it and types data
        enter_comments = self.find_element(searchLocators.SEARCH_COMMENTS)
        enter_comments.click()
        enter_comments.send_keys(comments)
        return enter_comments

    def click_on_the_submit_button(self): #submit data
        return self.find_element(searchLocators.SUBMIT_BUTTON, time=1).click() #finds element "submit" with searchLocators and clicks on it

```

TestFunc.py contains the discription of the test function's themselves. the Tests class implements the basic Factory pattern, the "client" function func enters data into the form's field and returns the result of the "creator" - func_type - function. func_type decides which of type of the test and calls whether for url checking or for alert catching function

```pytnon
import selenium
from PageObject import Feedback #imports Feedback class and functions from PageObject
from selenium.common.exceptions import NoAlertPresentException


class Tests():
    def catch_another_page(self, browser): #test if we stayed on Feedback.jsp
        return self.orig_url == self.mainPage.return_current_url(browser)

    def catch_alert_func(self, browser,): #test if we called for an alert window
        self.allert_exists=False
        try:
            alert = browser.switch_to.alert
            alert.accept()
            self.allert_exists=True
        except selenium.common.exceptions.NoAlertPresentException:
            pass
        return self.allert_exists

    def func_type(self,browser,t): #creator component of the factory pattern, that decides which type of the error we are dealing with
        if t==1:
            return self.catch_alert_func(browser)
        elif t==2:
            return self.catch_another_page(browser)

    def func(self,browser,name='',email='',subject='',comments='',t=''):  #main function for entering data (client component of the factory pattern)
        self.mainPage = Feedback(browser)
        self.mainPage.go_to_site()  # go to base_url sit
        self.orig_url = self.mainPage.return_current_url(browser)
        self.mainPage.enter_name(name)  # enters data in Your Name field
        self.mainPage.enter_email(email)  # enters data in Your Email Address field
        self.mainPage.enter_subject(subject)  # enters data in Subject field
        self.mainPage.enter_comments(comments)  # enters data in Question/Comment field
        self.mainPage.click_on_the_submit_button()
        return self.func_type(browser,t)
```
In the main file - start.py - we create functions with certain data for our tests.
```pytnon
from TestFunc import Tests

def test_altoro_feedback_only_name(browser,mainPage=Tests()): #tests if we can't send data without filling other important fields
    result = mainPage.func(browser, 'Sergey',t=2)
    assert result

def test_altoro_feedback_JS(browser,mainPage=Tests()): #test whether we can call for a JS alert window through Your Name field
    result = mainPage.func(browser,"<script>alert('attack')</script>",t=1)
    assert result

```
