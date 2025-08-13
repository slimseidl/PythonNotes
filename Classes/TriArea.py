class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()


    b1 = triangle1.set_base(float(input("Enter triangle 1 base:\n")))
    h1 = triangle1.set_height(float(input("Enter triangle 1 height:\n")))
      

    b2 = triangle2.set_base(float(input("Enter triangle 2 base:\n")))
    h2 = triangle2.set_height(float(input("Enter triangle 2 height:\n")))
      
    print('Triangle with smaller area:')  
    

    t1area = triangle1.get_area()
    t2area = triangle2.get_area()
    
    if t1area < t2area:
        triangle1.print_info()
    else:
        triangle2.print_info()
