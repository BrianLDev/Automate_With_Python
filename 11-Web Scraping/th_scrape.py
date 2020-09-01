# Scrape tiny house listing data from tinyhouselistings.com
import pandas as pd
import numpy as np
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ***** GLOBAL VARIABLES / INITIALIZE *****
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
urlCreated = False

# ***** FUNCTIONS *****
def createNewURL(searchCriteriaDict = {'page':'1'}):
    # Default is to pull ALL listings if searchCriteriaDict is left blank
    if len(searchCriteriaDict)==1:
        print("*** No search criteria added. Creating a URL to pull all listings...")
    else:
        print("*** Custom URL being build from search criteria inputs...")
    url = 'https://tinyhouselistings.com/search?'
    for key in searchCriteriaDict:
        if searchCriteriaDict[key] != '':
            url = url + '&' + str(key) + '=' + str(searchCriteriaDict[key])
    print("Custom search URL:  " + url)
    urlCreated = True
    return url

def createURL(searchCriteriaDict = {'page':'1'}):
    url = 'https://tinyhouselistings.com/search?'
    for key in searchCriteriaDict:
        if searchCriteriaDict[key] != '':
            url = url + '&' + str(key) + '=' + str(searchCriteriaDict[key])
    return url

def loadPage(url):
    try:
        driver.get(url)
        # driver.navigate(url)
        wait = WebDriverWait(driver, 10)
    except:
        print("Couldn't load url: " + url + "\nMay have reached the end of list")

def getListingsCount(url):
    print("*** Scraping listings count...")
    for i in range(1, 6):
        try:
            loadPage(url)
            results_count = driver.find_element_by_class_name('results-count')
            results_count = results_count.text
            results_count = results_count.split(' ')
            results_count = int(results_count[0])
            print("Listings total = " + str(results_count))
            return results_count
        except:
            print("Couldn't get count of listings.  Trying again.")

def getPageCount(listingsCount):
    print("*** Calculating page count...")
    pages = int(math.ceil(listingsCount / 12))
    print("Page total = " + str(pages))
    return pages

def getAllCardLinks(webElement):
    WebDriverWait(driver, 10)
    # WebDriverWait(driver).until(EC.presence_of_element_located((By.TAG_NAME, 'img')) )
    cards = driver.find_elements(By.CLASS_NAME, "listing-card-body")
    links = []
    for card in cards:
        links.append(card.find_element_by_tag_name('a').get_attribute('href') )
    return links

def scrapeSearchListingLinks(searchCriteriaDict = {'page':'1'}):
    # Loop through all pages of the search and collect links to listings
    listingLinksTemp = []
    pageLinks = []
    for i in range(1, page_count+1):
    # for i in range(7, 8):        #####################################################    FOR TESTING
        page = i
        print("*** Scraping links from page " + str(page))
        searchCriteriaDict['page'] = i
        search_url = createURL(searchCriteriaDict)
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
    print("DONE\n\nCount of Listings = " + str(len(listingLinksTemp)) )
    return listingLinksTemp

def scrapeListingData(links):
    listingDataCombined = pd.DataFrame()
    runningTotal = 0
    for link in links:
        listingDataTemp = pd.DataFrame()
        runningTotal += 1
        print("Scraping listing " + str(runningTotal) + " of " + str(len(links)) + ": " + link)
        loadPage(link)
        wait = WebDriverWait(driver, 10)
        hideZendeskPopup()
        for i in range(1, 6):
            try:
                # Get name and price from the top section
                name = driver.find_element_by_class_name('listing-right-title').text
                listingDataTemp['Name'] = pd.Series(name)
                listingDataTemp['Price'] = driver.find_element_by_class_name('listing-price').text
                # Get location and split into City, State, Country
                location = driver.find_element_by_class_name('listing-location-string').text
                listingDataTemp['Location'] = pd.Series(str(location).strip(), dtype='string')
                locationSplit = str(location).split(", ")
                for location in locationSplit:
                    location = location.strip() # remove leading and trailing whitespace
                listingDataTemp['City'] = pd.Series([locationSplit[0]], dtype='string')
                listingDataTemp['State'] = pd.Series([locationSplit[1]], dtype='string')
                listingDataTemp['Country'] = pd.Series([locationSplit[2]], dtype='string')
                # Get type, foundation, misc from listingDetailsStack
                listingDetailsStack = driver.find_element_by_class_name('listing-details-stack')
                listingDetailsValues = listingDetailsStack.find_elements_by_tag_name('h4') # values of type, foundation, misc
                listingDataTemp['Type'] = listingDetailsValues[0].text
                listingDataTemp['Foundation'] = listingDetailsValues[1].text
                listingDataTemp['Misc'] = listingDetailsValues[2].text
                # Get all the remaining data from the listingDetailsTable.  Usually has 2 of them per page.
                listingDetailsTable = driver.find_elements_by_class_name('listing-details-table')
                for table in listingDetailsTable:
                    listingDetailsKeys = table.find_elements_by_class_name('detail-key')
                    listingDetailsValues = table.find_elements_by_class_name('detail-value')
                    for i in range(0, len(listingDetailsKeys)):
                        key = listingDetailsKeys[i].text
                        value = listingDetailsValues[i].text
                        listingDataTemp[key] = value
                break
            except:
                print("Couldn't scrape listing data, trying again. Attempt " + str(i) + " of 5")
        listingDataTemp['Link'] = link
        # Add individual listing to DataFrame of listings
        if (listingDataCombined.empty):
            listingDataCombined = listingDataTemp
        else:
            listingDataCombined = listingDataCombined.append(listingDataTemp)
    # Ensure that Link is the last column and return the DataFrame
    dfTemp = listingDataCombined.pop('Link')
    listingDataCombined['Link'] = dfTemp
    print("DONE\n\nTotal count of listings: " + str(listingDataCombined.shape[0]) )
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
        if (string == math.nan or string == 'nan' or string == ''):  # checks if string is empty
            pass
        else:
            print("Couldn't isolate value on: " + string)

def isolateValuesInSeries(seriesOfStrings):
    seriesOfValues = seriesOfStrings.apply(lambda x : isolateValue(x) )
    return seriesOfValues

def validateColumns(df):
    print("*** Validating columns...")
    correctColumns = ['Name', 'Price', 'Location', 'City', 'State', 'Country', 'Type', 'Foundation', 'Misc', 'Bedrooms', 'Lofts', 'Bathrooms', 
                        'Size', 'Length', 'Width', 'Days on site', 'Number of views', 'Times dreamlisted', 'Link']
    for col in correctColumns:
        if col not in df.columns:
            print("- Found a missing column: " + col + ".  Adding it now")
            df[col] = pd.Series(dtype=int) # create an empty column with the missing column name
    # Ensure that Link is the last column and return the DataFrame
    dfTemp = df.pop('Link')
    df['Link'] = dfTemp
    print("DONE")
    return df

def cleanData(df):
    df = validateColumns(df)
    # Clean up data formatting and isolate values
    print("*** Cleaning, reformatting data and isolating values from text...")
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
    print("DONE")
    return df

def makeSubdirectory(name):
    import os
    if os.path.exists(name) == False:
        try:
            print("*** Making subdirectory to save scrapes: " + name)
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
    print("*** Saving records to csv format in subdirectory: " + subdirectoryName)
    makeSubdirectory(subdirectoryName)
    dateStamp = getDateStamp()
    listingData.to_csv(subdirectoryName + "/" + "TH Listings " + dateStamp + ".csv", header=True, index=False)
    print("DONE")


# ***** INPUT SEARCH OPTIONS *****
# Leave an item blank to ignore it in the search filter
# To choose multiple within the same category, put '%2C' between them (e.g. '&purchase_type=purchase%2Cmodel')
# The URL builder function will use the '&' symbol as needed to include a search term
# TODO: CREATE AN INPUT FUNCTION SO I CAN CUSTOMIZE SEARCH TERMS WITHOUT HAVING TO CHANGE THE SCRIPT
searchOptionsDict = {
    'price_min': '10000',         # Includes cents
    'price_max': '5000000',       # Includes cents
    'area_min': '200',
    'area_max': '700',            # The website slider maxes out at 700 so this may be a limit?  Will need to test
    'purchase_type': 'purchase',  # Options are: 'purchase' 'rent' 'model'.  Connect multiple with the also keyword below
    'location_type': 'mobile',    # Options are:  'mobile' 'stationary' 'floating'
    'property_type': '',          # Options are: 'tiny_house' 'cabin boat' 'rv' 'converted_bus' 'other' 'land' 'camper' 'container_home' 'tiny_house_shell' 'apartment' 'tiny_house_trailer' 'park_model
    'bedrooms_min': '',
    'bedrooms_max': '',
    'bathrooms_min': '',
    'bathrooms_max': '',
    'page': '1'
}

# ***** RUN SCRIPTS *****
time_start = time.time()
print("\n\n***** 1. CREATING A CUSTOMIZED SEARCH URL *****\n")
# TODO: Add ability to select search type outside of script editing
# UNCOMMENT ONE OF THE TWO OPTIONS BELOW TO EITHER RUN A FULL OR A FILTERED SCRAPE
# OPTION 1:
# search_url = createNewURL(searchOptionsDict)   # Scrape data based on custom search criteria above (or from input)
# OR OPTION 2:
search_url = createNewURL()                    # Scrape data from ALL listings

# Get listing and page counts
print("\n\n***** 2. GETTING ORIGINAL LISTING COUNT AND CALCULATING PAGE COUNT *****\n")
listings_count = getListingsCount(search_url)
page_count = getPageCount(listings_count)

# Scrape the data and hold it in a DataFrame
print("\n\n***** 3. SCRAPING LISTING LINKS FROM SEARCH QUERY *****\n")
listingLinks = scrapeSearchListingLinks()
print("\n\n***** 4. SCRAPING DATA FROM INDIVIDUAL LISTING PAGES *****\n")
listingData = scrapeListingData(listingLinks)

# Clean data
print("\n\n***** 5. CLEAN AND REFORMAT THE DATA *****\n")
listingData = cleanData(listingData)

# Save as a csv export in a subfolder
print("\n\n***** 6. SAVE AND EXPORT TO CSV *****\n")
folder = 'th_scrapes'
saveToCSV(folder)

# Summary
print("\n")
print("************* SCRAPE COMPLETE *************\n")
print("Listings scraped: " + str(listingData.shape[0]) + " out of " + str(listings_count) + " (" + str(round(listingData.shape[0] / listings_count * 100, 2)) + "%)" )
valuesScraped = np.sum(listingData.count())
valuesMax = (listings_count * listingData.shape[1])
print("Values scraped*: " + str(valuesScraped) + " out of " + str(valuesMax) + " (" + str(round(valuesScraped / valuesMax * 100, 2)) + "%)" )
print("   *Excludes blank or null values")
time_end = time.time()
seconds = round(time_end - time_start,2)
minutes = round(seconds / 60, 2)
if (minutes > 1):
    print("\nTotal minutes to run script: " + str(minutes))
else:
    print("\nTotal seconds to run script: " + str(seconds))
seconds_per_listing = round(seconds / listingData.shape[0], 2)
print("Average seconds per listing: " + str(seconds_per_listing))
print("\n*******************************************\n\n")

# Done
driver.quit()