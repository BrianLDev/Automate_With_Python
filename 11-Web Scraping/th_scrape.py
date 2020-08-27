# Scrape tiny house listing data from tinyhouselistings.com

import requests, bs4

# res = requests.get('https://tinyhouselistings.com/search?area_min=240&price_max=4500000&price_min=100&purchase_type=purchase&page=1')
# try:
#     res.raise_for_status()
#     print("success")
#     searchPage = bs4.BeautifulSoup(res.text, features="html.parser")
#     print(searchPage.)
# except Exception as exc:
#     print('There was a problem: %s' % exc)

res2 = requests.get('https://tinyhouselistings.com/listings/large-tiny-house-for-kids-tiny_house-mobile')
try:
    res2.raise_for_status()
    print("success")
    tinyHomePage = bs4.BeautifulSoup(res2.text, features="html.parser")
    print(tinyHomePage.contents)
    spans = tinyHomePage.select('div span')
    print(len(spans))
    print(spans[0])
except Exception as exc:
    print('Error: %s' % exc)