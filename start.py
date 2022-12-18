from PageObject import Feedback #imports Feedback class and functions from PageObject


def test_altoro_feedback_only_name(browser): #first test
    mainPage = Feedback(browser) #initialize object as Feedback class with base_url and driver attributes
    mainPage.go_to_site() #go to base_url site
    mainPage.enter_name("Sergey") #enters data in Your Name field
    mainPage.click_on_the_submit_button()
    check_url=mainPage.return_current_url(browser) #saves current url
    assert 'Feedback.jsp' in check_url #checks if we stayed in the same website url or not

def test_altoro_feedback_wrong_email(browser): #second test
    mainPage = Feedback(browser) #initialize object as Feedback class with base_url and driver attributes
    mainPage.go_to_site() #go to base_url sit
    mainPage.enter_name("ⁿⁿⁿ") #enters data in Your Name field
    mainPage.enter_email("ⁿⁿⁿ@ⁿⁿⁿ.ⁿⁿⁿ") #enters data in Your Email Address field
    mainPage.enter_subject("ⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿ") #enters data in Subject field
    mainPage.enter_comments("ⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿⁿ") #enters data in Question/Comment field
    check_url = mainPage.return_current_url(browser) #saves current url
    assert 'Feedback.jsp' in check_url #checks if we stayed in the same website url or not

def test_blank_email_address(browser): #third test
    mainPage = Feedback(browser) #initialize object as Feedback class with base_url and driver attributes
    mainPage.go_to_site() #go to base_url sit
    mainPage.enter_name("123")  #enters data in Your Name field
    mainPage.enter_email(" @ . ") #enters data in Your Email Address field
    check_url = mainPage.return_current_url(browser) #saves current url
    assert 'Feedback.jsp' in check_url #checks if we stayed in the same website url or not
