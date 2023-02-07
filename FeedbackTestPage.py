from BasePage import BasePage
from BaseElement import Locator
from Logger import Logg


class Feedback(BasePage):
    FeedbackLogger = Logg("FeedbackLogger")
    def enter_name(self,name): #find Your Name field, clicks on it and types data in it
        name_field = self.find_element(Locator.SEARCH_FIELD_YOUR_NAME)
        self.FeedbackLogger.makeLog("SiteLogger")
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def enter_email(self,email):#find Your Email Address field, clicks on it and types data in it
        email_field = self.find_element(Locator.SEARCH_FIELD_YOUR_EMAIL)


    def enter_subject(self,subject): #finds Subject field, clicks on it and types data in it
        subject_field = self.find_element(Locator.SEARCH_SUBJECT)  #
        self.enter_data(subject_field, subject)

    def enter_comments(self,comments): #finds Question/Comment field, clicks on it and types data
        comment_field = self.find_element(Locator.SEARCH_COMMENTS)

        self.enter_data(comment_field, comments)


    def click_on_the_submit_button(self): #submit data
         self.find_element(Locator.SUBMIT_BUTTON).click() #finds element "submit" with searchLocators and clicks on it



