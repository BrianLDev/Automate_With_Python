

inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inv):
    count = 0
    print("Inventory:")
    for i in inv.items():
        print(str(i[1]) + " " + str(i[0]))
        count += i[1]
    print("\nTotal number of items: " + str(count))

displayInventory(inventory)