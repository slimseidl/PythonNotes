def max_magnitude(x, y, z):
    return max([x,y,z], key=abs)  
    # key tells python to use absolute value but still return the original value 


a = int(input("Enter first value:\n"))
b = int(input("Enter second value:\n"))
c = int(input("Enter third value:\n"))

print(f'The max magnitude is: {max_magnitude(a,b,c)}')