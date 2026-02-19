class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
    def display(self):
        print("Brand:", self.Brand)
        print("Model:", self.Model)

car1=Car("hunda", "civic")
car1.display()

# inheritance
class ElectricCar(Car):
    def __init__(self, Brand, Model, BatterySize):
        super().__init__(Brand, Model)
        self.BatterySize = BatterySize
    def display(self):
        super().display()
        print("Battery Size:", self.BatterySize)
ElectricCar1=ElectricCar("tesla","xqwe",100
                         )
ElectricCar1.display()