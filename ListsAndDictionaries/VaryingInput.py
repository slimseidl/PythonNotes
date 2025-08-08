my_list = [int(i) for i in (input("Enter your numbers:\n").split())]
average = int(sum(my_list) / len(my_list))
maxlist = max(my_list)

print(f'The average is {average}, The max is: {maxlist}')