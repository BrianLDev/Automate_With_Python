def printPicnic(itemsDict, leftWidth=0, rightWidth=0):    
    # add section to autocalculate the left and right width based on the max length of the data in itemsDict
    if(leftWidth <=0):
        for x in itemsDict.keys():
            if leftWidth < len(x) + 2:
                leftWidth = len(x) + 2
    if(rightWidth <=0):
        for x in itemsDict.values():
            if rightWidth < len(str(x)) + 1:
                rightWidth = len(str(x)) + 1

    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    print('\n')

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems)

picnicItems = {'tacos': 3, 'cup': 2, 'blanket': 1, 'bottle of wine': 1, 'fancy wine glasses': 2}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems)