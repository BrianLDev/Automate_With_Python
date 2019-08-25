# II - Automating Tasks
## 07 - Regular Expressions (RegEx)

#### Answers to Practice Questions

1. re.compile() returns Regex objects

2. Because raw strings save you from having to double backslash \\\ escape characters

3. search() returns the first match as a Match Object?  

4. to get the strings from a match object, you need to use the group() method

5. group 0 covers all groups combined, group 1 covers the area code, and group 2 covers the regular phone number

6. to match actual ( and . characters, you would need to put a backslash in front of them

7. I'm not sure...
XXX
If the regex has no groups, a list of strings is returned.  If the regex has groups, a list of tuples of strings is returned.

8. OR

9. ? can mean optional and it can also mean nongreedy matching  

10. The + character means the preceding item is mandatory (one or more times) and the * is match the precedign item zero or more times

11. {3} means match 3 of the preceeding group, and {3,5} means match between 3 and 5 of the preceeding group

12. \d means digit, \w means word, \s means space characters

13. \D, \W, and \S mean the absence of the above

14. re.IGNORECASE

15. the . character is a wildcard for all characters except newline \\n.  and re.DOTALL matches all characters including newlines

16. .* means zero or more wildcard, and .? means wildcard is optional
XXX
.* is a greedy match and .? is a nongreedy match

17. [0-9a-z]

18. 'X drummers, X pipers, five rings, X hens'

19. re.VERBOSE ignores whitespace in the regex equation so you can make complex regex formulas easier for humans to read

20. re.compile(r'(\d?\d?\d?)*,?(\d?\d?\d)')
XXX
re.compile(r'^\d{1,3}(,\d{3})*$')

21. re.compile(r'[A-Z]\w\sNakamoto')

22. re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)

#### SCORE:  
18.5/22 = 100%