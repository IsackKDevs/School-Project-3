


class Inventory:
    def __init__(self, name, purchase_price, value_in_5yrs, annual_depreciation):
        self.itemname= name
        self.Purchase_Price = purchase_price
        self.Value_in_5_years = value_in_5yrs
        self.annual_depreciation = annual_depreciation

    def itemname(name):
        return name
    def Purchase_Price(purchase_price):
        return purchase_price
    def Value_in_5_years(value_in_5_years):
        return value_in_5_years
    def annual_depreciation(self, purchase_price, value_in_5yrs ):
        purchase_price = self.Value_in_5_years()
        value_in_5yrs = self.Value_in_5_years()
        annual_depreciation = (purchase_price - value_in_5yrs)/5
        return annual_depreciation


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