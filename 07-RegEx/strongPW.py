# strongPW.py
# Checks a string to see if it is considered a strong password: 8+ characters long, upper and lower, and contains at least 1 digit
# Uses RegEx to do the test

import re

upperRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]*')
digitRegex = re.compile(r'\d*')

print("\nEnter a password that you want to test to see if it is strong: ")
password = input()

lenChk = len(password) >= 8
upperChk = upperRegex.search(password)
lowerChk = lowerRegex.search(password)
digitChk = digitRegex.search(password)

print(str(lenChk) + str(len(upperChk)>0) + str(lowerChk) + str(digitChk))