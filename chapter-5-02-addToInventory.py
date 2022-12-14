from hi import displayInventory

def addToInventory(listOfItems):
    inventory = {}

    for value in listOfItems:
        """
        if inventory:
            inventory[value] += 1
        else:
            inventory[value] = 1
        """
        inventory.setdefault(value, 0)
        inventory[value] += 1
    return inventory


givenListOfItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# print(addToInventory(givenListOfItems))

displayInventory(addToInventory(givenListOfItems))