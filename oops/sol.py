class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model
    def display(self):
        print("Brand:", self.Brand)
        print("Model:", self.Model)