# Program for Items in a shopping cart with subtotal, sales tax, and grand total
class ItemToPurchase():
    def __init__(self, item_name="none", item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        print(f'Item Cost:\n{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity:.2f}')
        
    def get_total(self):
        return self.item_price * self.item_quantity
    
    def get_sales_tax(self):
        return (self.item_price * self.item_quantity) * .07



item_count = 0
subtotal = 0
while True:
    stop = input("Enter 'quit' to stop adding items to cart or any other key to continue:\n")
    if stop == 'quit':
        break
    item_count +=1
    print(f'Item {item_count}:')

    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    qty = int(input("Enter the item quantity:\n"))
    item = ItemToPurchase(name, price, qty)



    item.print_item_cost()
    subtotal += item.get_total()
sales_tax = subtotal * .07
total = subtotal + sales_tax

print(f"Subtotal: ${subtotal:.2f}\nTax: ${sales_tax:.2f}\nGrand Total: ${total:.2f}")


    
# print("Item 1")
# name1 = input("Enter the item name:\n")
# price1 = float(input("Enter the item price:\n"))
# qty1 = int(input("Enter the item quantity:\n"))
# item1 = ItemToPurchase(name1, price1, qty1)

# print("\nItem 2")
# name2 = input("Enter the item name:\n")
# price2 = float(input("Enter the item price:\n"))
# qty2 = int(input("Enter the item quantity:\n"))
# item2 = ItemToPurchase(name2, price2, qty2)

    


    
    