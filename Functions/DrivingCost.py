# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost =  (miles_driven / miles_per_gallon) * dollars_per_gallon
    return cost 

if __name__ == '__main__':
    # Type your code here.
    
    print(f'Enter miles per gallon:')
    mpg = float(input())
    print(f'Enter cost per gallon of gas:')
    dpg = float(input())
    print(f'Enter miles driven:')
    miles = int(input())

    print(f'The cost of driving {miles} miles in this vehicle is: ${driving_cost(mpg, dpg, miles):.2f}')
