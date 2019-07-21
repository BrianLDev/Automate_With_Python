

def list_to_string(listIn):
    listString = ""
    for l in listIn:
        listString += str(l) + ", "
        if l == listIn[-2]:
            listString += "and "

spam = ['apples', 'bananas', 'tofu', 'cats']

list_to_string(spam)