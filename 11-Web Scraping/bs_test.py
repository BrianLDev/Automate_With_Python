# Testing out beautiful soup 4 HTML parser
#
# Examples of selectors:
# soup.select('div')                    HTML tags
# soup.select('#author')                ID's
# soup.select('p #author')              ID's within HTML tags
# soup.select('.notice')                HTML classes
# soup.select('div span')               Tags within tags
# soup.select('div > span')             Tags within and immediately following a tag
# soup.select('input[name]')            input that matches the name
# soup.select('input[type="button"]')   inputs of a specitif type

import requests, bs4


url="https://content-creator-site-template.netlify.app/"
website = requests.get(url)
try:
  website.raise_for_status()

  savefile = open('bstest.html', 'wb') # wb = write binary.  Required even for text data
  for chunk in website.iter_content(100000):
    savefile.write(chunk)
  savefile.close()
  
  # Can create a beautiful soup object either with a saved HTML file or directly from the request response
  soup = bs4.BeautifulSoup(website.text, 'html.parser') #bs4 now warns you to specify a parser
  # soup = bs4.BeautifulSoup(open('bstest.html'), 'html.parser') #bs4 now warns you to specify a parser

  print("*******")
  print("Nav items:")
  navItems = soup.select('.nav-item')
  for item in navItems:
    print("Nav Item found: " + item.getText() )
  print("*******")
  print("Card Attributes:")
  cards = soup.select('.card')
  for card in cards:
    print(card.attrs)
  print("*******")

  print("Done")


except Exception as exc:
    print('There was a problem: %s' % (exc))