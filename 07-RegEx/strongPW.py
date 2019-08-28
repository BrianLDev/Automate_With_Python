# strongPW.py
# Checks a string to see if it is considered a strong password: 8+ characters long, upper and lower, and contains at least 1 digit
# Uses RegEx to do the test

import re

upperRegex = re.compile(r'[A-Z]+')
lowerRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')

print("\nEnter a password that you want to test to see if it is strong: ")
password = input()

lenChk = len(password) >= 8
upperChk = upperRegex.search(password) != None
lowerChk = lowerRegex.search(password) != None
digitChk = digitRegex.search(password) != None

if lenChk and upperChk and lowerChk and digitChk:
    print("\nStrong Password!\n")
else:
    print("\nNot so Strong...")
if not lenChk:
    print("   *** Must be 8+ characters ***")
if not upperChk:
    print("   *** Must have at least 1 capital letter ***")
if not lowerChk:
    print("   *** Must have at least 1 lowercase letter ***")
if not digitChk:
    print("   *** Must have at least 1 digit ***")

# Trying out Kyle from SPAR's code
KyleRegex = re.compile(r'^[A-Za-z0-9]{8}$')
KyleResult = KyleRegex.search(password) != None
print("\nKyle Regex Test = " + str(KyleResult) + "\n")