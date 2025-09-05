# Write a program whose input is two integers. 
# Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer. 
# End with a newline.

num1 = int(input())
num2 = int(input())
total = 0

if num1 > num2:
    print('Second integer can\'t be less than the first.')
else:
    while num1 <= num2:
        print(num1,end=' ')
        num1+=5
    print()