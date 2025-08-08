char_list = input('Enter a character and a phrase\n').split()

charCountVar = char_list[0]
total = 0

for word in char_list[1:]:
    total += word.count(charCountVar)

if total == 1:
    print(f'There is {total} {charCountVar} in this phrase.')
else:
    print(f'There are {total} {charCountVar}\'s in this phrase.')