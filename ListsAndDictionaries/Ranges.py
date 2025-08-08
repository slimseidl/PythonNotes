my_list = [int(i) for i in input("Enter some integers:\n").split()]

numRange = [int(i) for i in input("Enter upper and lower bounds:\n").split()]

print(f'The numbers within the upper and lower bounds in your list are: ')
for i in my_list:
    if i >= min(numRange) and i <= max(numRange):
        print({i}, end=' ')
