from BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from importlib import reload
logging.shutdown()
reload(logging)
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")





class Feedback(BasePage):
    SEARCH_FIELD_YOUR_NAME = (By.NAME, "name")  # creates locator for Your Name field
    SEARCH_FIELD_YOUR_EMAIL = (By.NAME, "email_addr")  # creates locator for Your Email Address field
    SEARCH_SUBJECT = (By.NAME, "subject")  # creates locator for YSubject field
    SEARCH_COMMENTS = (By.NAME, "comments")  # creates locator for Question/Comment field
    SUBMIT_BUTTON = (By.NAME, "submit")  # creates locator for submit button
    def enter_name(self,name): #find Your Name field, clicks on it and types data in it
        name_field = self.find_element(self.SEARCH_FIELD_YOUR_NAME)
        logger = logging.getLogger()
        logger.info("1")
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def enter_email(self,email):#find Your Email Address field, clicks on it and types data in it
        enter_email = self.find_element(self.SEARCH_FIELD_YOUR_EMAIL)
        enter_email.click()
        enter_email.send_keys(email)
        return enter_email

    def enter_subject(self,subject): #finds Subject field, clicks on it and types data in it
        enter_subject = self.find_element(self.SEARCH_SUBJECT)  #
        enter_subject.click()
        enter_subject.send_keys(subject)
        return enter_subject

    def enter_comments(self,comments): #finds Question/Comment field, clicks on it and types data
        enter_comments = self.find_element(self.SEARCH_COMMENTS)
        enter_comments.click()
        enter_comments.send_keys(comments)
        return enter_comments

    def click_on_the_submit_button(self): #submit data
        return self.find_element(self.SUBMIT_BUTTON, time=1).click() #finds element "submit" with searchLocators and clicks on it



