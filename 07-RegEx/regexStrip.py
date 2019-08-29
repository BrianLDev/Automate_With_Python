# regexStrip.py

# Regex Version of strip() 
# Write a function that takes a string and does the same thing as the strip() 
# string method. If no other arguments are passed other than the string to 
# strip, then whitespace characters will be removed from the beginning and 
# end of the string. Otherwise, the characters specified in the second 
# argument to the function will be removed from the string.

import re

def strip(sourceStr, chars = r'(^\s*)|(\s*$)'):
    sourceStr = str(sourceStr)
    chars = str(chars)
    print(sourceStr)
    newStr = re.sub(chars, '', sourceStr)
    return(newStr)

print(strip("   Bananas are full of potassium   ") )
print('\n')
print(strip("Remove the swear words you asshole", "asshole") )
