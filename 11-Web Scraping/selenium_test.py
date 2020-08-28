from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# BL Note: The book uses Firefox for this, but MacOS Catalina makes it near impossible with all their security hoops.  
# Using Safari instead (also don't have to install anything with safari)
# To use safari with selenium you need to enable Remote automation.  2 ways to do this:
# 1) in terminal type `safaridriver --enable`
# 2) In safari preferences, turn on Developer options, then in Developer options enable remote automation

browser = webdriver.Safari()
wait = WebDriverWait(browser, 10)
print(type(browser))
browser.get('http://inventwithpython.com')

# ***** FUNCTIONS *****
def openPageNewBrowser(url):
    browser.get(url)

# def openPageNewTab(url):
    # MAY NOT BE POSSIBLE IN SELENIUM
    # webdriver.ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.RETURN).perform() # Key combo
    # browser.findElement(By.linkText("urlLink")).sendKeys(selectLinkOpeninNewTab);

def getElements():
    # for more info, see https://www.selenium.dev/documentation/en/webdriver/web_element/
    try:
        # *** OLD WAY ***     
        # elem = browser.find_element_by_class_name('card-img-top')
        # linkElem = browser.find_element_by_id('minecraft')
        # linkElem = browser.find_element_by_link_text("See what's new in the second edition.")

        # *** NEW WAY ***
        linkElem = browser.find_element(By.linkText("See what's new in the second edition.") )

        print('Found <%s> element.' % type(linkElem))

        return linkElem
    except:
        print("Was not able to find that element.")

def click(linkElem):
    linkElem.click()  # follows the link  # Note - Click isn't working in Safari. Known issue so I'll need to work around it

def loginTest():
    browser.get('https://mail.yahoo.com')
    emailElem = browser.find_element_by_id('login-username')
    emailElem.send_keys('not_my_real_email')
    passwordElem = browser.find_element_by_id('login-passwd')
    passwordElem.send_keys('12345')
    passwordElem.submit()

def keysTest():
    # For more info see https://www.selenium.dev/documentation/en/webdriver/keyboard/
    htmlElem = browser.find_element_by_tag_name('html')
    # htmlElem.send_keys(Keys.HOME) #scrolls to the top
    htmlElem.send_keys(Keys.END) #scrolls to the bottom
    # htmlElem.send_keys(Keys.ENTER) #Hit enter

def popupAlert():
    browser.find_element(By.LINK_TEXT, "See an example alert").click() # Click the link to activate the alert
    alert = wait.until(expected_conditions.alert_is_present()) # Wait for the alert to be displayed and store it in a variable
    text = alert.text # Store the alert text in a variable
    # alert.send_keys("response to message prompt if there is one")
    # alert.dismiss() # Press the Cancel button
    alert.accept() # Press the OK button
    # webdriver.ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").perform() # Key combos

def back():
    browser.back()

def forward():
    browser.forward()

def refresh():
    browser.refresh()

def quit():
    browser.quit()


# ***** DEMO *****
getElements()
keysTest()
browser.get('https://yahoo.com')
back()
keysTest()
wait = WebDriverWait(browser, 3)
forward()
browser.get('https://google.com')
wait = WebDriverWait(browser, 10)
search_box = browser.find_element(By.NAME, "q")
search_box.send_keys("Boo!  I am controlling your keyboard." + Keys.ENTER)
# quit()