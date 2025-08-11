import random
        
number = random.randint(1,100)
guesses = 1
num = int(input("Guess a number between 1 and 100:\n"))
while guesses <= 5:
    
    if num < number:
        print('Higher')
    elif num > number:
        print(f'Lower')
    elif num == number:
        print(f'{num} is correct!')
        break
    else:
        print('Error')
    guesses += 1
    num = int(input())

else:
    print('You suck!')
    print(f'The correct answer was {number}')
