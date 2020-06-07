import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt', 'wb') # wb = write binary. required even when saving text data

    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    playFile.close()
    print("Romeo and Juliet successfully saved")
except Exception as exc:
    print('There was a problem: %s' % (exc))
