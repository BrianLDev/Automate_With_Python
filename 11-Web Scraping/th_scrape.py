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
    for i in range(1, page_count+1):
    # for i in range(7, 8):        ###########    FOR TESTING
        page = i
        search_url = url1 + str(page) + url2
        print("*** Scanning page " + str(page))
        print(search_url)
        loadPage(search_url)
        wait = WebDriverWait(driver, 50)

        pageLinks = None
        while(not pageLinks):
            pageLinks = getAllCardLinks(search_url)
            if not pageLinks:
                print("No cards found on page.  Trying again")
                wait = WebDriverWait(driver, 50)
        
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
        for i in range(1, 6):
            try:
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
                break
            except:
                print("Couldn't scrape listing data, trying again. Attempt " + str(i) + "/5")
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
        if not str(string): # checks if string is empty
            pass
        else:
            print("Couldn't isolate value on: " + string)

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

def validateColumns(df):
    correctColumns = ['Name', 'Price', 'Location', 'Type', 'Foundation', 'Misc', 'Bedrooms', 'Lofts', 'Bathrooms', 'Size', 'Length', 'Width', 'Days on site', 'Number of views', 'Times dreamlisted', 'Link']
    for col in correctColumns:
        if col not in df.columns:
            print("Found a missing column: " + col + ".  Adding it now")
            df[col] = pd.Series()
    # Ensure that Link is the last column and return the DataFrame
    dfTemp = df.pop('Link')
    df['Link'] = dfTemp
    return df

def cleanData(df):
    df = validateColumns(df)
    # Clean up data formatting and isolate values
    print("Cleaning up formatting and isolating values...")
    df['Price'] = isolateValuesInSeries(df['Price'])
    df['Bedrooms'] = isolateValuesInSeries(df['Bedrooms'])
    df['Lofts'] = isolateValuesInSeries(df['Lofts'])
    df['Bathrooms'] = isolateValuesInSeries(df['Bathrooms'])
    df['Size'] = isolateValuesInSeries(df['Size'])
    df['Length'] = isolateValuesInSeries(df['Length'])
    df['Width'] = isolateValuesInSeries(df['Width'])
    df['Days on site'] = isolateValuesInSeries(df['Days on site'])
    df['Number of views'] = isolateValuesInSeries(df['Number of views'])
    df['Times dreamlisted'] = isolateValuesInSeries(df['Times dreamlisted'])
    return df

def makeSubdirectory(name):
    import os
    if os.path.exists(name) == False:
        try:
            print("Making subdirectory to save scrapes: " + name)
            os.mkdir(name)
        except OSError as error:
            print(error)

def getDateStamp():
    from datetime import datetime
    date = datetime.now()
    # dateStamp = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + str(date.minute)
    dateStamp = str(date)
    dateStamp = dateStamp.replace(':', '_')
    return dateStamp

def saveToCSV(subdirectoryName):
    print("Saving records to csv format in subdirectory: " + subdirectoryName)
    makeSubdirectory(subdirectoryName)
    dateStamp = getDateStamp()
    listingData.to_csv(subdirectoryName + "/" + "TH Listings " + dateStamp + ".csv", header=True, index=False)


# ***** SCRIPT *****
# Run scrapes
page_count = getPageCount(search_url)
listingLinks = scrapeSearchListingLinks()
listingData = scrapeListingData(listingLinks)
print("\n** Total count of listings: " + str(listingData.shape[0]))

folder = 'th_scrapes'
saveToCSV(folder)
# Clean daeta
listingData = cleanData(listingData)

# Save data
saveToCSV(folder)
print("\n***** SCRAPE COMPLETE *****\n")

# Done
driver.quit()