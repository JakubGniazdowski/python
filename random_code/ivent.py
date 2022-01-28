def addtoinventory(inventory,lootlist):
    for i in range(len(lootlist)):
        if lootlist[i] in inventory:
            inventory[lootlist[i]] = inventory[lootlist[i]] + 1

    else:
        inventory.setdefault(lootlist[i],1)

        return inventory


def displayinventory(inventory):
    total_items = 0

    for k,v in inventory.items():
        print(k + ' : ' + str(v))

        total_items = total_items + v

    print("Total number of items: " + str(total_items))


    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addtoinventory(inv, dragonLoot)
    displayinventory(inv)