from invetory import Inventory



def main():
    ItemName = "x"
    ItemCount = 0
    
    def moreitems():
        more_items = input("More items? y/n ")
        if more_items == "y":
            name = Inventory(input("Enter Item: "), int(input("Enter Price ")), int(input("Value in 5 yrs: ")),"")
            ItemCount =+ 1
            return True
        else:
            return False
    return moreitems()

main()