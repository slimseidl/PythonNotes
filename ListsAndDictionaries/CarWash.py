services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

print('ZyCar Wash')
print('Base car wash -- $10')
choice1 = input()
choice2 = input()
total+= base_wash

if choice1 != '-':
    print(f'{choice1} -- ${services[choice1]}')
    total+= services[choice1]
if choice2 != '-':
    print(f'{choice2} -- ${services[choice2]}')
    total+= services[choice2]
    
print(f'----')
print(f'Total price: ${total}')


# OR Second way is better

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = base_wash

print('ZyCar Wash')
print('Base car wash -- $10')

choices = [input(), input()]

for choice in choices:
    if choice != '-':
        print(f'{choice} -- ${services[choice]}')
        total += services[choice]

print(f'----')
print(f'Total price: ${total}')
