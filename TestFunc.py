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

