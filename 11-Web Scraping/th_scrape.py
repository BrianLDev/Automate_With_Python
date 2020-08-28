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
        listingDetailsStack = driver.find_element_by_class_name('listing-details-stack') # the stack that holds type, foundation, misc
        listingDetailsValues = listingDetailsStack.find_elements_by_tag_name('h4') # values of type, foundation, misc
        listingDataTemp['Type'] = listingDetailsValues[0].text
        listingDataTemp['Foundation'] = listingDetailsValues[1].text
        listingDataTemp['Misc'] = listingDetailsValues[2].text
        listingDetailsTable = driver.find_elements_by_class_name('listing-details-table') # the table(s) that contain the rest of the data.  Usually 2 tables
        for table in listingDetailsTable:
            listingDetailsKeys = table.find_elements_by_class_name('detail-key')
            listingDetailsValues = table.find_elements_by_class_name('detail-value')
            for i in range(0, len(listingDetailsKeys)):
                key = listingDetailsKeys[i].text
                value = listingDetailsValues[i].text
                listingDataTemp[key] = value
        listingDataTemp['Link'] = link
        # Add individual listing to DataFrame of listings
        if (listingDataCombined.empty):
            listingDataCombined = listingDataTemp
        else:
            listingDataCombined = listingDataCombined.append(listingDataTemp)
    # Ensure that Link is the last column and return the DataFrame
    dfTemp = listingDataCombined.pop('Link')
    listingDataCombined['Link'] = dfTemp
    return listingDataCombined

def isolateValue(string):
    try:
        string = str(string) # ensure that everything is a string
        if '$' in string:
            string = string.replace('$', '')
            string = string.replace(',', '')
            value = int(string)
        elif ' ' in string:
            if '.' in string:
                value = float(str(string).split(' ')[0] )
            else:
                value = int(str(string).split(' ')[0] )
        else:
            if '.' in string:
                value = float(string)
            else:
                value = int(string)
        return value
    except:
        print("Couldn't isolate value on: " + string)
        pass

def isolateValuesInSeries(seriesOfStrings):
    seriesOfValues = seriesOfStrings.apply(lambda x : isolateValue(x) )
    return seriesOfValues

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

def makeSubdirectory(name):
    import os
    if os.path.exists(name) == False:
        try:
            os.mkdir(name)
        except OSError as error:
            print(error)

def getDateStamp():
    from datetime import datetime
    date = datetime.now()
    # dateStamp = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + str(date.minute)
    dateStamp = str(date)
    dateStamp = dateStamp.replace(':', '_')
    print(dateStamp)
    return dateStamp


# ***** SCRIPT *****
page_count = getPageCount(search_url)
listingLinks = scrapeSearchListingLinks()
listingData = scrapeListingData(listingLinks)

listingData['Price'] = isolateValuesInSeries(listingData['Price'])
listingData['Bedrooms'] = isolateValuesInSeries(listingData['Bedrooms'])
listingData['Lofts'] = isolateValuesInSeries(listingData['Lofts'])
listingData['Bathrooms'] = isolateValuesInSeries(listingData['Bathrooms'])
listingData['Size'] = isolateValuesInSeries(listingData['Size'])
listingData['Length'] = isolateValuesInSeries(listingData['Length'])
listingData['Width'] = isolateValuesInSeries(listingData['Width'])
listingData['Days on site'] = isolateValuesInSeries(listingData['Days on site'])
listingData['Number of views'] = isolateValuesInSeries(listingData['Number of views'])
listingData['Times dreamlisted'] = isolateValuesInSeries(listingData['Times dreamlisted'])

print("/n** Total count of listings: " + str(listingData.shape[0]))

subdirectoryName = 'th_scrapes'
makeSubdirectory(subdirectoryName)

dateStamp = getDateStamp()
listingData.to_excel(subdirectoryName + "/" + "Tiny House Listings " + dateStamp + ".xlsx", header=True, index=False)

driver.quit()
