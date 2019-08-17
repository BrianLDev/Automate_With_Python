#Take a 2 dimensional nested table and print it out in nice columns, right justified, with each sublist item matched with the corresponding other sublist items

def printTable(table):
    # first get the max length for each of the 3
    colWidths = [0] * len(table)    # creates a list of 0 variables for reach sublist in table
    for i in range(0, len(table)):
        for x in table[i]:
            if colWidths[i] < len(x)+1:
                colWidths[i] = len(x)+1

    # now print out the data
    for rowNum in range(0, len(table[0])):
        rowString = ""
        for colNum in range(0, len(table)):
            rowString += str(table[colNum][rowNum].rjust(colWidths[colNum]))
        print (rowString)
    print ("\n")

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

tableData = [['apples', 'oranges', 'cherries', 'banananutBandit'],
             ['Alice', 'Beelzebub', 'Carol', 'David'],
             ['doggers', 'cats', 'moose', 'goose'],
             ['green', 'orange', 'red', 'black/white']]

printTable(tableData)