from TestFunc import Tests

def test_altoro_feedback_only_name(browser,mainPage=Tests()): #tests if we can't send data without filling other important fields
    result = mainPage.func(browser, 'Sergey',t=2)
    assert result

def test_altoro_feedback_JS(browser,mainPage=Tests()): #test whether we can call for a JS alert window through Your Name field
    result = mainPage.func(browser,"<script>alert('attack')</script>",t=1)
    assert result
