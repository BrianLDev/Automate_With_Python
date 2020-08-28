# Scrape tiny house listing data from tinyhouselistings.com
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ***** GLOBAL VARIABLES / INITIALIZE *****
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

url1 = 'https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page='
page = '1'
url2 = '&price_max=5000000&price_min=100&purchase_type=purchase'
'https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page=10&price_max=5000000&price_min=100&purchase_type=purchase'
search_url = url1 + page + url2


# ***** FUNCTIONS *****
def loadPage(url):
    try:
        driver.get(url)
        # driver.navigate(url)
        wait = WebDriverWait(driver, 10)
    except:
        print("Couldn't load url: " + url + "\nMay have reached the end of list")

def getAllCardLinks(webElement):
    WebDriverWait(driver, 10)
    # WebDriverWait(driver).until(EC.presence_of_element_located((By.TAG_NAME, 'img')) )
    cards = driver.find_elements(By.CLASS_NAME, "listing-card-body")
    links = []
    for card in cards:
        links.append(card.find_element_by_tag_name('a').get_attribute('href') )
    return links

def getPageCount(url):
    loadPage(url)
    results_count = driver.find_element_by_class_name('results-count')
    print(results_count)
    results_count = results_count.text
    results_count = results_count.split(' ')
    results_count = int(results_count[0])
    print("Results total = " + str(results_count))
    pages = int(math.ceil(results_count / 12))
    print("Page total = " + str(pages))
    return pages

def scrapeSearchListingLinks():
    print("\n***** SCRAPING LISTING LINKS FROM SEARCH QUERY *****")
    # Loop through all pages of the search and collect links to listings
    listingLinksTemp = []
    pageLinks = []
    # for i in range(1, page_count+1):
    for i in range(1, 2): #Delete this when done testing
        page = i
        search_url = url1 + str(page) + url2
        print("*** Scanning page " + str(page))
        print(search_url)
        loadPage(search_url)
        wait = WebDriverWait(driver, 10)

        pageLinks = getAllCardLinks(search_url)
        for link in pageLinks:
            listingLinksTemp.append(link)
            print(link)
    print("Final item count = " + str(len(listingLinksTemp)) )
    return listingLinksTemp

def scrapeListingData(links):
    print("\n***** SCRAPING DATA FROM INDIVIDUAL LISTING PAGES *****")
    listingDataCombined = pd.DataFrame()

    for link in links:
        listingDataTemp = pd.DataFrame()
        print("Scraping data from: " + link)
        loadPage(link)
        wait = WebDriverWait(driver, 10)
        hideZendeskPopup()
        name = driver.find_element_by_class_name('listing-right-title').text
        listingDataTemp['Name'] = pd.Series(name)
        listingDataTemp['Price'] = driver.find_element_by_class_name('listing-price').text
        listingDataTemp['Location'] = driver.find_element_by_class_name('listing-location-string').text
        listingDetailsStack = driver.find_element_by_class_name('listing-details-stack') # the stack that holds type, foundation, delivery
        listingDetailsValues = listingDetailsStack.find_elements_by_tag_name('h4') # values of type, foundation, delivery
        listingDataTemp['Type'] = listingDetailsValues[0].text
        listingDataTemp['Foundation'] = listingDetailsValues[1].text
        listingDataTemp['Delivery'] = listingDetailsValues[2].text
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # listingDataTemp[''] = 
        # TODO: GATHER OTHER DATA
        if (listingDataCombined.empty):
            listingDataCombined = listingDataTemp
        else:
            listingDataCombined = listingDataCombined.append(listingDataTemp)
    return listingDataCombined

def hideZendeskPopup():
    try:
        xpath = '//*[@id="Embed"]/div/div/div/div/div/div/div[1]/div/button[2]/svg'
        xpathFull = '/html/body/div[1]/div/div/div/div/div/div/div/div/div[1]/div/button[2]/svg'
        # driver.switch_to_frame(driver.find_element_by_id("webWidget")
        zendesk = driver.find_element_by_xpath(xpath)
        # driver.switch_to_frame(zendesk)
        zendesk.click()
        print (' !! Zendesk popup Squashed !!')
    except:
        # print('.. No zendesk popup ..')
        pass


# ***** SCRIPT *****
page_count = getPageCount(search_url)
listingLinks = scrapeSearchListingLinks()
listingData = scrapeListingData(listingLinks)

print("** Total count of listings: " + str(listingData.shape[0]))
for delivery in list(listingData['Delivery']):
    print(delivery)

# TODO: EXPORT PANDAS DATAFRAME TO CSV OR EXCEL

driver.quit()
