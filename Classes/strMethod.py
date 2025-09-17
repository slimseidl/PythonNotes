class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return (f'{self.year} {self.make} {self.model}:\n  Mileage: {self.miles}\n  Sticker price: ${self.price}')# ... This line will cause error until method is implemented

cars = []
cars.append(Car('Ford', 'F150;', 2013, 150000, 13500))
cars.append(Car(input(), input(), int(input()), int(input()), int(input())))
cars.append(Car(input(), input(), int(input()), int(input()), int(input())))

for car in cars:
    print(car)