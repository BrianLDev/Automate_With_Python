# 01 - Python Programming Basics
## 04 - Lists

#### Answers to Practice Questions

1. `[]` are brackets that indicate a list

2. `spam.insert('hello', 2)` or   
`spam[2] = 'hello'`

**For the following 3 questions, spam contains the list `['a', 'b', 'c', 'd']`**

3. `spam[int(int('3' * 2) / 11)]` evaluates to 3 which is `'d'`

4. `spam[-1]` indicates the last item in the list which is also `'d'`

5. `spam[:2]` is a slice that grabs 2 items from the list, item 0 and item 1 whih is `['a', 'b']`

**For the following 3 questions, bacon contains the list `[3.14, 'cat', 11, 'cat', True]`**

6. `bacon.index('cat')` evaluates to a tuple `(1, 3)`  
XXX - looks like it just pulls the index of the first value found  
`(1)`

7. `bacon.append(99)` evaluates to `[3.14, 'cat', 11, 'cat', True, 99]`

8. would change the list to `[3.14, 11, True]`  
XXX - The second cat would remain  
`[3.14, 11, 'cat', True]` 

9. list concatenate: `+`  
list replication: `=` or `*`

10. append() adds the item at the end of the list, while insert() wedges the item into the list at a specific index

11. you can remove values from a list by using either `listName.remove(index)` or `del ListName[index]`

12. List values are similar to string values because they're both a sequence of values.  In a string its a sequence of characters.  
XXX  
Also, they can be used with `len()`, have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

13. Lists are mutable and use [], while tuples are immutable and use ()

14. `meaningOfEverything = (42, )`

15. `tuple(ListName)`  
`list(tupleName)`

16. they contain references to the values

17. copy.copy() makes a copy of the list but not any nested lists.  copy.deepcopy() also includes any nested lists

#### SCORE:  
14 / 17 = 82%