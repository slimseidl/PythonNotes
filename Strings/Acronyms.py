phrase = input("Enter a phrase to create an acronym:\n")
words = phrase.split()
print(f'Your acronym for {phrase} is:\n')

for i in words:
    if i[0].isupper():
        print(f'{i[0]}.',end="")
    else:
        continue

