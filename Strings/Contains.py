char = input("Enter a character to search for in a list of words:\n")
words = input("Enter a phrase or list of words:\n").split()

print(f'{char} is in these words:\n')

for i in words:
    if char in i:
        print(i)
    else:
        continue

