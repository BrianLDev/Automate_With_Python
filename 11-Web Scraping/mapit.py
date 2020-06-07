#! python3
# mapIt.py - Luanches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from the command line
    address = '+'.join(sys.argv[1:])
else:
    # Get address from the clipboard
    address = pyperclip.paste()

print("address = " + address)
webbrowser.open('https://www.google.com/maps/place/' + address)
