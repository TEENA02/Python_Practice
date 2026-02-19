class Car:
    total_cars=0
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
        Car.total_cars += 1
    def display(self):
        print("Brand:", self.Brand)
        print("Model:", self.Model)
    def speed_calculate(self, speed):
        return f"The speed of the {self.Brand} {self.Model} is {speed} km/h"
    
car1=Car("hunda", "civic")
car2=Car("toyota", "corolla")
car3=Car("ford", "mustang")
print(car2.total_cars)
print(Car.total_cars)


# inheritance
class ElectricCar(Car):
    def __init__(self, Brand, Model, BatterySize):
        super().__init__(Brand, Model)
        self.BatterySize = BatterySize
    def display(self):
        super().display()
        print("Battery Size:", self.BatterySize)
    def speed_calculate(self, speed):
        return f"The speed of the {self.Brand} {self.Model} is {speed} km/h"
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
# static method -method defined inside a class 
# that does not depend on any instance or class data.
class cal:
    @staticmethod
    def mul(a,b):
        return a*b

print(cal.mul(100,34))

# property decorator - allows us to define methods 
# that can be accessed like attributes

