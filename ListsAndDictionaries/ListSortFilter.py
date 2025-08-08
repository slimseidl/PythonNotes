my_list = sorted([int(i) for i in input("Enter some numbers to sort:\n").split()])

print('The sorted non-negative integers are:\n')
for i in my_list:
    if i >= 0:
        print(i, end=' ')
