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


# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group() )


# Matching zero or more with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group() )
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group() )


# Matching one or more with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group() )
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group() )
mo3 = batRegex.search('The Adventures of Batman')
print(mo3)


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


# The finadall() Method
