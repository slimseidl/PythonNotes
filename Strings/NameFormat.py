name = input('Please enter your name:\n')

tokens = name.split()

if len(tokens) == 3:
    firstName = tokens[0]
    midName = tokens[1]
    lastName = tokens[2]
    print(f'{lastName}, {firstName[0].upper()}.{midName[0].upper()}.')
else:
    firstName = tokens[0]
    lastName = tokens[1]
    print(f'Your formatted name is:\n{lastName}, {firstName[0].upper()}.')