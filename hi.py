# Using it to import some functions to other files
def displayInventory(inventory):
    totalObjects = 0
    print("Inventory: ")
    for key, value in inventory.items():
        print(value, key)
        totalObjects += value
    print(f"Total number of items: {totalObjects}")


givenInventory = {'rope': 1, 'torch': 6,
                  'gold coin': 42, 'dagger': 1, 'arrow': 12}

# displayInventory(givenInventory)

