

def isPhoneNumber(text):
    """
    Checks if a block of text is a phone number
    Note that this isn't able to handle odd formatting like 415.222.5555 or 415-222-5555 x74
    This is the beginning part of the RegEx Chapter to eventually show how much easier and better this will be using RegEx instead
    """
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

var1 = '415-555-4242'
var2 = 'Moshi moshi'

print(var1 + " is a phone number:\n" + str(isPhoneNumber(var1)))
print(var2 + " is a phone number:\n" + str(isPhoneNumber(var2)))

message = "Call me at 415-555-1010 tomorrow.  415-555-9999 is my office."
print ("\n" + message)
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")


## REGEX VERSION
import re
# regex without using the r for raw
# phoneNumRegex = re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
# regex using the r for raw (no need for double \\)
# phoneNumRegex = re.compile( r'\d\d\d-\d\d\d-\d\d\d\d')
# regex using groups
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# match object (mo) tries to find a phone number in the text
mo = phoneNumRegex.search(' My number is 415-555-4242.')
# name the groups
areaCode, mainNumber = mo.groups()

print('Phone number found (regex): ' + mo.group(0) )
print(mo.group(1))
print(mo.group(2))

