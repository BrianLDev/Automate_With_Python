

def list_to_string(listIn):
    listString = ""
    for l in listIn:
        listString += str(l)
        if(listIn.index(l) < len(listIn) - 2):
            listString += ", "
        elif l == listIn[-2]:
            listString += ", and "
    print(listString)

spam = ['apples', 'bananas', 'tofu', 'cats']
list_to_string(spam)

spam2 = [13, 'Heyyyyy', 'massive', 123.456, (1, 2, 3)]
list_to_string(spam2)