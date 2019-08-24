# Project: Phone Number and Email Address Extractor

#! python3 
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard. 

import pyperclip, re 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code 
    (\s|-|\.)?                      # separator 
    (\d{3})                         # first 3 digits 
    (\s|-|\.)                       # separator 
    (\d{4})                         # last 4 digits 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE) 
    
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+_]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z])                    # dot-something
    )''', re.VERBOSE)
 
# TODO: Find matches in clipboard text. 
 
# TODO: Copy results to the clipboard.


