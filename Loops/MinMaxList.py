num = int(input("Enter a number, any number:\n"))
num_list = []

while num > 0:
    num_list.append(num)
    num = int(input("Enter another number:\n"))
    
print(f'{min(num_list)} is the min and {max(num_list)} is the max')