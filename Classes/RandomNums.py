from random import randint

class RandomNumbers:
    def __init__(self):
        self.var1= 0
        self.var2= 0
        self.var3= 0
    
    def get_var1(self):
        return self.var1
        
    def get_var2(self):
        return self.var2
        
    def get_var3(self):
        return self.var3
        
    def set_random_values(self, low, high):
        self.var1 = randint(low,high)
        self.var2 = randint(low,high)
        self.var3 = randint(low,high)
        
    def get_random_values(self):
        print(f'Random values: {self.var1} {self.var2} {self.var3}')
        
    

if __name__ == "__main__":
    low = int(input())
    high = int(input())

    numbers = RandomNumbers()
    numbers.set_random_values(low, high)
    numbers.get_random_values()