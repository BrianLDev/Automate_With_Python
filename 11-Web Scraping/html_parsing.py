import requests, bs4

res = requests.get('http://nostarch.com')
try:
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")
    print("Type = " + str(type(noStarchSoup)) )
except Exception as exc:
    print('There was a problem: %s' % exc)