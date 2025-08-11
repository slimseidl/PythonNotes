# Split input into 2 parts: name and age
parts = input("Enter a name followed by a space, then an age or enter -1 to terminate:\n ").split()
name = parts[0]
while name != '-1':

    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    
        
    except ValueError as excpt:
        print(f'{name} 0')
    
    
    finally:

        parts = input().split()
        name = parts[0]