change = int(input())

if change <= 0:
    print("No change")
else:
    dollars = change // 100
    change %= 100
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")
    
    quarters = change // 25
    change %= 25
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")
    
    dimes = change // 10
    change %= 10
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")
        
    nickels = change // 5
    change %= 5
    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")
        
    pennies = change
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")
