class Car:
    def __init__(self, Year = None, Mileage = None, Price = None):
        self.year = int(Year)
        self.mileage = int(Mileage)
        self.price = int(Price)

    def __str__(self):
        return f'Year: {self.year}, Mileage: {self.mileage}, Price: {self.price}'


    def __lt__(self,rightCar):
        return self.year < rightCar.year