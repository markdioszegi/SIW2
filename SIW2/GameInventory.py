import os
import sys

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inv):
    for item in inv:
        print("{}: {}".format(item, inv[item]))

def add_to_inventory(inv, added_items):
    for item in added_items:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1

def sortDictionary(inv, rev):
    inv = sorted(inv.items(), key=lambda k: k[1], reverse=rev)
    inv = dict(inv)
    return inv
            
def print_table(inv, order = "empty"):
    print("-----------------")
    print("item name | count")
    print("-----------------")
    if order == "count,desc":
        inv = sortDictionary(inv, 1)
        for item in inv:
            print("{:>9} | {:>5}".format(item, inv[item]))
    elif order == "count,asc":
        inv = sortDictionary(inv, 0)
        for item in inv:
            print("{:>9} | {:>5}".format(item, inv[item]))
    elif order == "empty":
        for item in inv:
            print("{:>9} | {:>5}".format(item, inv[item]))
    else:
        print("Wrong argument!")
    print("-----------------")

def import_inventory(inv, filename = "import_inventory.csv"):
    try:
        with open(os.path.join(sys.path[0], filename), "r", encoding="Utf-8") as f:
            tmp = f.readline().split(",")
            f.close()
        add_to_inventory(inv, tmp)
    except FileNotFoundError:
        print("File {} not found!".format(filename))

def export_inventory(inv, filename):
    try:
        with open(os.path.join(sys.path[0], filename), "w") as f:
            tmp = []
            for item in inv:
            #tmp.append((item + ",") * inv[item])
                for i in range(inv[item]):
                    tmp.append(item)
            #print(tmp)
            #exit()
            f.write(",".join(tmp))
            f.close()
    except PermissionError:
        print("You don't have permission creating file {}!".format(filename))

add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print_table(inv, "count,desc")
import_inventory(inv, "import_inventory.csv")
print_table(inv, "count,desc")
export_inventory(inv, "export_inventory.csv")