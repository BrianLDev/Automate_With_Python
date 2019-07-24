# 1st Challenge - Create a fantasy Inventory using a Dictionary and then display the inventory with a count of total items at the end

inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inv):
    count = 0
    print("\nInventory:")
    for i in inv.items():
        print(str(i[1]) + " " + str(i[0]))
        count += i[1]
    print("\nTotal number of items: " + str(count))

displayInventory(inventory)


# 2nd Challenge - create a fuction that lets you add items to the dictionary inventory.  But the added items are in list format.

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1    # works both ways
        #inventory[item] = inventory[item] + 1  # works both ways
    return inventory

inventory = {'gold coin': 42, 'rope': 1}
displayInventory(inventory)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)