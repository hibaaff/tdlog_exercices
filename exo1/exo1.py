"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""
class Item:
    def __init__(self,weight,price):
        self.weight=weight 
        self.price=price
        
    def get_price(self):
        print('price:',self.price)
    def get_weight(self):
        print('weight:',self.weight)

i=Item(10,20)

i.get_price()
