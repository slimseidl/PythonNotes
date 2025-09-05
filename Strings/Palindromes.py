text = input()

if text.replace(" ","") == text[::-1].replace(" ",""):
    print(f'{text} is a palindrome')
else:
    print(f'{text} is not a palindrome')

# Second Way
text = input()
tokens = text.split()
new_text = ''.join(tokens)

if new_text == new_text[::-1]:
    print(f'{text} is a palindrome')
else:
    print(f'{text} is not a palindrome')