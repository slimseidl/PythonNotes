low = int(input("Enter the lower bound:\n"))
high = int(input("Enter the upper bound:\n"))
x = int(input("Enter a multiple to test:\n"))
counter = 0
for i in range(low, high+1):
    if i % x == 0:
        counter+=1
    else:
        continue
    
print("Number of multiples of ", x,":", counter)
        