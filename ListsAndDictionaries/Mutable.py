# Enter a list of numbers with a space between then swap the first and last values and output

user_values = input().split()
user_values = [int(i) for i in user_values]

user_values[0], user_values[-1] = user_values[-1], user_values[0]

for val in user_values:
    print(val, end=" ")
print()
