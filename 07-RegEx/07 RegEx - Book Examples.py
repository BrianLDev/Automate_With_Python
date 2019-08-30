# II - Automating Tasks
## 07 - Regular Expressions (RegEx)

#### Book Examples from Chapter

"""
Goes through all the various examples and use cases of regex from the book
"""
import re

# Matching Multiple groups with the Pipe
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.') # takes the first match
print(mo1.group() )
mo2 = heroRegex.search('Tina Fey and Batman.') # takes the first match
print(mo2.group() )

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group() )
print(mo.group(1) )
print('*************')


# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group() )
print('*************')


# Matching zero or more with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group() )
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group() )
print('*************')


# Matching one or more with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group() )
mo3 = batRegex.search('The Adventures of Batman')
print(mo3)
print('*************')


# Matching Specific Repetitions with Curly Brackets
haRegex = re.compile(r'(Ha){3}')
mo1  = haRegex.search('HaHaHa')
print(mo1.group() )
mo2 = haRegex.search('Ha')
print(mo2)
haRegex = re.compile(r'(Ha){2,4}')
mo3 = haRegex.search('HaHaHaHa')
print(mo3.group() )
mo4 = haRegex.search('HaHaHaHaHaHaHaHaHaHa')
print(mo4.group() )
print('*************')


# Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group() )
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group() )
print('*************')


# The finadall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # returns a list of strings
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # with groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')) # returns a list of tuples of strings
print('*************')


# Character Classes
"""
Examples of shorthand character classes:
\d = any numberic digit
\D = any character NOT a digit
\w = any word (letters, numeric digit, or underscore)
\W = NOT a word (e.g. whitespace)
\s = any space, tab, or newline
\S = NOT any space, tab or newline
"""
xmasRegex = re.compile(r'\d+\s\w+')
xmasList = xmasRegex.findall(' 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmasList)
vowelRegex = re.compile( r'[aeiouAEIOU]')
print(vowelRegex.findall(' RoboCop eats baby food. BABY FOOD!'))
consonantRegex = re.compile(r'[^aeiouAEIOU ]') # ^ symbol at beginning means NOT any of the characters in the brackets
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD!'))
beginsWithHello = re.compile(r'^Hello')  # in is case the ^ symbol at the beginning means that this text must be found at the beginning
print(beginsWithHello.search('Hello  world!'))
print(beginsWithHello.search('He said hello.'))
endsWithNumber = re.compile( r'\d$') # the $ symbol at end searches for the digit at the end
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.'))
wholeStringIsNum = re.compile( r'^\d+$')  # the ^ at beginning and $ at end means it has to start and end with digits, and the + means it has to be in the middle.  So full string of digits
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890'))
print(wholeStringIsNum.search('12 34567890'))
print('*************')


# The Wildcard Character
atRegex = re.compile(r'.at')  #uses the . wildcard symbol to match any character before 'at'
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # uses .* wildcard to match all characters (except newline)
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() )
print('*')
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group() )
print('*************')


# Review of Regex Symbols
print("""
Review of Regex Symbols  
This chapter covered a lot of notation, so here’s a quick review of what you learned: 
- The ? matches zero or one of the preceding group. 
- The * matches zero or more of the preceding group. 
- The + matches one or more of the preceding group. 
- The {n} matches exactly n of the preceding group. 
- The {n,} matches n or more of the preceding group. 
- The {, m} matches 0 to m of the preceding group. 
- The {n, m} matches at least n and at most m of the preceding group. 
- {n, m}? or *? or +? performs a nongreedy match of the preceding group. 
- ^spam means the string must begin with spam. spam $ means the string must end with spam. 
- The . matches any character, except newline characters. 
- \d, \w, and \s match a digit, word, or space character, respectively. 
- \D, \W, and \S match anything except a digit, word, or space character, respectively. 
- [abc] matches any character between the brackets (such as a, b, or c). 
- [^abc] matches any character that isn’t between the brackets.
""")
print('*************')


# Case Insensitive Matching
robocop = re.compile( r'robocop', re.I)  # the re.I 2nd argument makes this regex case insensitive
print(robocop.search('RoboCop is part man, part machine, all cop.').group() )
print(robocop.search('ROBOCOP protects the innocent.'). group() )
print(robocop.search('Al, why does your programming book talk about robocop so much?'). group() )
print('*************')


# Substituting Strings with the sub() method
namesRegex = re.compile(r'Agent \w+')
print("Agent Alice gave the secret documents to Agent Bob.")
print(namesRegex.sub('REDACTED', "Agent Alice gave the secret documents to Agent Bob."))
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print("Agent Eve told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(agentNamesRegex.sub(r'\1****', "Agent Eve told Agent Carol that Agent Eve knew Agent Bob was a double agent."))
print('*************')


# Managing Complex Regexes
phoneRegex = re.compile( r'''( 
    (\ d{ 3} |\(\ d{ 3}\))?                 # area code 
    (\ s |-|\.)?                            # separator 
    \d{ 3}                                  # first 3 digits 
    (\ s |-|\.)                             # separator 
    \d{ 4}                                  # last 4 digits 
    (\ s*( ext | x | ext.)\ s*\ d{ 2,5})?   # extension 
    )''', re.VERBOSE) # re.VERBOSE ignores the whitespace above that is used to make it easier to format and visualize complex regexes

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile(' foo', re.IGNORECASE | re.DOTALL)  # two options combined
someRegexValue = re.compile(' foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # three options combined
