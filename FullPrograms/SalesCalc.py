order = 1
sales_total = 0.00

# Run the while loop
while True:
    try:
        line = input("Enter carpet price/sqft, room width, and room length separated by a space or 'enter' to quit:\n").strip() # check for blank input / end of input
    except EOFError:
        break
    
    if not line:
        break
    
    print(f'Order #{order}')
    price, width, length = map(float,line.split())
    area = int(length * width)
    carpet_cost = area * price * 1.20
    print(f'Room: {area} sq ft')
    print(f'Carpet: ${carpet_cost:.2f}')
    
    
    labor = 0.75 * area
    print(f'Labor: ${labor:.2f}')
    
    
    tax = (labor + carpet_cost) * .07
    total_cost = tax + labor + carpet_cost
    print(f'Tax: ${tax:.2f}')
    print(f'Cost: ${total_cost:.2f}')
    print()
    
    sales_total += total_cost
    order += 1

print(f'Total Sales: ${sales_total:.2f}')