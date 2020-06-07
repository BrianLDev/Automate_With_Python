import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    print("Type = " + str(type(res)) )
    print("Status Code = " + str(res.status_code == requests.codes.ok) )
    print("Len = " + str(len(res.text)) )
    print(res.text[:250])
except Exception as exc:
    print('There was a problem: %s' % (exc))


print("*****************")

res2 = requests.get('https://automatetheboringstuff.com/page_that_does_not_exist')
try:
    res2.raise_for_status()
    print("Type = " + str(type(res2)) )
    print("Status Code = " + str(res2.status_code == requests.codes.ok) )
    print("Len = " + str(len(res2.text)) )
    print(res2.text[:250])
except Exception as exc:
    print('There was a problem: %s' % (exc))

