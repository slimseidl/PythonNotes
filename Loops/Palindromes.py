num = int(input("Enter an integer between 11 and 100:"))

while 11 <= num <= 100:
    if str(num) == str(num)[::-1]:
        print(num)
        break
    else:
        print(num)
        num-=1
else:
    print("Input must be 11-100")