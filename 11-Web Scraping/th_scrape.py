# Scrape tiny house listing data from tinyhouselistings.com
import pandas as pd
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ***** FUNCTIONS *****
def loadPage(url):
    try:
        driver.get(url)
        # driver.navigate(url)
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

def getPageCount():
    results_count = driver.find_element_by_class_name('results-count')
    print(results_count)
    results_count = results_count.text
    results_count = results_count.split(' ')
    results_count = int(results_count[0])
    print("Results total = " + str(results_count))
    pages = int(math.ceil(results_count / 12))
    print("Page total = " + str(pages))
    return pages

def scrapeAllListingLinks():
    # Loop through all pages of the search and collect links to listings
    combinedLinks = []
    pageLinks = []
    for i in range(1, page_count+1):
        page = i
        search_url = url1 + str(page) + url2
        print("*** Scanning page " + str(page))
        print(search_url)
        loadPage(search_url)
        wait = WebDriverWait(driver, 10)

        pageLinks = getAllCardLinks(search_url)
        for link in pageLinks:
            combinedLinks.append(link)
            print(link)
    return combinedLinks


# ***** SCRIPT *****
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)

url1 = 'https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page='
page = '1'
url2 = '&price_max=5000000&price_min=100&purchase_type=purchase'
'https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page=10&price_max=5000000&price_min=100&purchase_type=purchase'
search_url = url1 + page + url2
loadPage(search_url)

page_count = getPageCount()

allLinks = scrapeAllListingLinks()

print("Final item count = " + str(len(allLinks)) )

# TODO: SCRAPE DATA FROM ALL INDIVIDUAL LISTING PAGES
# TODO: PUT SCRAPED LISTING DATA INTO PANDAS DATAFRAME
# TODO: EXPORT PANDAS DATAFRAME TO CSV OR EXCEL

driver.quit()
