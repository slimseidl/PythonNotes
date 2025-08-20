loanAmount = float(input())
payment = float(input())
rate = float(input())
pmtCount = 0

while loanAmount > 0:
    loanAmount += (loanAmount * rate)
    loanAmount -= payment
    pmtCount += 1
    
if pmtCount == 1:
    print(f'{pmtCount} payment')
else:
    print(f'{pmtCount} payments')