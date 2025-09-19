car_bal = 18995.26
truck_bal = 10502.30

carPmt = 462.50
truckPmt = 1050.00

num_of_payments = 4
car_payments = 0

while truck_bal > 0:
    truck_bal -= truckPmt
    car_bal -= carPmt
    num_of_payments += 1
else:
    car_payments += num_of_payments
    while car_bal > 0:
        car_bal -= 1400
        car_payments += 1


print(f'Truck Payments: {num_of_payments}')
print(f'Car Payments: {car_payments}')

saved = 0
months = 0
car_value = 25000

if truck_bal <=0 and car_bal <= 0:
    # for i in range(0,12):
    #     saved += (carPmt + truckPmt)
    while saved < 25000:
        months +=1
        saved+= (truckPmt + carPmt)




print(f'Months to save: {months}')
print(f'Total saved: {saved}')
print(f'Trade Value: {saved + car_value}')


