link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector('button.btn:nth-child(3)')

    assert button, "not element"