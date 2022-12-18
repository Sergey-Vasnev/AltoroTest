from BaseApp import BasePage
from selenium.webdriver.common.by import By

class searchLocators: #locators class
    SEARCH_FIELD_YOUR_NAME = (By.NAME, "name") #creates locator for Your Name field
    SEARCH_FIELD_YOUR_EMAIL = (By.NAME, "email_addr") #creates locator for Your Email Address field
    SEARCH_SUBJECT = (By.NAME, "subject") #creates locator for YSubject field
    SEARCH_COMMENTS = (By.NAME, "comments") #creates locator for Question/Comment field
    SUBMIT_BUTTON = (By.NAME, "submit") #creates locator for Your Name field

class Feedback(BasePage):
    def enter_name(self,name): #find Your Name field and enter  data
        name_field = self.find_element(searchLocators.SEARCH_FIELD_YOUR_NAME) #find Your Name field by its "name" value
        name_field.click() #click on found field to activate typing
        name_field.send_keys(name) #type data in field
        return name_field

    def enter_email(self,email):#find Your Email Address field and enter  data
        enter_email = self.find_element(searchLocators.SEARCH_FIELD_YOUR_EMAIL)#find Your Email Address field by its "name" value
        enter_email.click() #click on found field to activate typing
        enter_email.send_keys(email) #type data in field
        return enter_email

    def enter_subject(self,subject):
        enter_subject = self.find_element(searchLocators.SEARCH_SUBJECT) #find Subject field by its "name" value
        enter_subject.click() #click on found field to activate typing
        enter_subject.send_keys(subject) #type data in field
        return enter_subject

    def enter_comments(self,comments):
        enter_comments = self.find_element(searchLocators.SEARCH_COMMENTS) #find Question/Comment field by its "name" value
        enter_comments.click() #click on found field to activate typing
        enter_comments.send_keys(comments) #type data in field
        return enter_comments

    def click_on_the_submit_button(self): #submit data
        return self.find_element(searchLocators.SUBMIT_BUTTON, time=1).click() #finds element "submit" and clicks on it