mylist = input("Enter a name followed immediately by a comma and a phone number, then repeat to build a contact list:\n").split()
contacts = {}

for val in mylist:
    names,numbers = val.split(',')
    contacts[names] = numbers

search = input("Enter a person's name to search for their number:\n")

print(f'{search}\'s number is {contacts[search]}')