values = input().split()
values = [float(i) for i in values]
maxVal = max(values)
values = [(i / maxVal) for i in values]

for num in values:
    print(f'{num:.2f}', end=" ")
    
print()