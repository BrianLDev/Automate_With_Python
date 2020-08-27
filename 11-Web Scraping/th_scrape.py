# Scrape tiny house listing data from tinyhouselistings.com

import requests, bs4

def website_request(url, saveFileName=""):
    website = requests.get(url)
    try:
        website.raise_for_status()
        print("successfully loaded page: " + url)
        if saveFileName != "":
            with open(saveFileName, 'wb') as file:  # using with open() allows you to skip close() on the file after you're done with it
                for chunk in website.iter_content(100000):
                    file.write(chunk)
        return website
    except Exception as exc:
        print('There was a problem: %s' % exc)


url = 'https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page=1&price_max=5000000&price_min=100&purchase_type=purchase'

website = website_request(url, 'th_search.html')

cards = website.select('.listing-card')
print(cards)

# res2 = requests.get('https://tinyhouselistings.com/listings/large-tiny-house-for-kids-tiny_house-mobile')
# try:
#     res2.raise_for_status()
#     print("success")
#     tinyHomePage = bs4.BeautifulSoup(res2.text, features="html.parser")
#     print(tinyHomePage.contents)
#     spans = tinyHomePage.select('div span')
#     print(len(spans))
#     print(spans[0])
# except Exception as exc:
#     print('Error: %s' % exc)
