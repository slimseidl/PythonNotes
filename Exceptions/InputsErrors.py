try:
    count = 0
    values = []
    
    val1 = int(input())
    values.append(val1)
    count += 1
    
    val2 = int(input())
    values.append(val2)
    count += 1
    
    val3 = int(input())
    values.append(val3)
    count += 1
    
    print(max(values))
    
except:
    if len(values) > 0:
        print(f'{count} input(s) read:')
        print(f'Max is {max(values)}')
    else:
        print(f'{count} input(s) read:')
        print(f'No max')