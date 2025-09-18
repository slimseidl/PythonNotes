import math

class Pythagorean():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def find_c(self):
        hypotenuse = math.sqrt((math.pow(self.a,2)+math.pow(self.b,2)))
        return hypotenuse
    
    def find_a(self):
        csq = math.pow(self.c,2)
        bsq = math.pow(self.b,2)
        a = math.sqrt(csq-bsq)
        return a 
    
    def find_b(self):
        csq = math.pow(self.c,2)
        asq = math.pow(self.a,2)
        b = math.sqrt(csq-asq)
        return b
    

triangle = Pythagorean()

    # Finding Hypotenuse
# triangle.a = float(input("Enter leg 'a' of the right triangle:\n"))
# triangle.b = float(input("Enter leg 'b' of the right triangle:\n"))
# print(f'Hypotenuse: {triangle.find_c():.2f}')

# Finding Side a
triangle.c = float(input("Enter hypotenuse of the right triangle:\n"))
triangle.b = float(input("Enter leg 'b' of the right triangle:\n"))
a = triangle.find_a()
print(f'Side "a" of the right triangle: {a:.2f}')