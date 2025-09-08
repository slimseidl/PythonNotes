purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

item = input()
qty = int(input())

if qty > 20:
    print(f'{item} ${((purchase[item] * qty) * .90):.2f}')
elif 10 <= qty <= 20:
    print(f'{item} ${((purchase[item] * qty) * .95):.2f}')
else:
    print(f'{item} ${(purchase[item] * qty):.2f}')