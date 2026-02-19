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

#encapsulation
class Chanel:
    def __init__(self, perfume_name, Price, Quantity):
        self.perfume_name=perfume_name
        self._Price=Price
        self.__Quantity=Quantity
    def get_quantity(self):
        return self.__Quantity
    def display(self):
        return f"perfume_name:{self.perfume_name},Price:{self._Price},Quantity:{self.__Quantity}"
class Chanel1(Chanel):
    def __init__(self, perfume_name, Price, Quantity, Discount):
        super().__init__(perfume_name, Price, Quantity)
        self.Discount=Discount
    def display_details(self):
        print(self.perfume_name, self._Price, self.get_quantity(), self.Discount)  
my_perfume=Chanel1("coco", 100, 50, 10)
my_perfume.display_details()

# polymorphism-olymorphism allows same method, function or operator
# to behave differently depending on object it is working with
