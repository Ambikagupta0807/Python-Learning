class car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def full_name(self):
        return f"{self.brand} {self.name}"
    def fuel_type(self):
        return "Petrol or diesel"

class electric_car:
    def __init__(self,brand,bttry_size):
        self.brand = brand
        self.bttry_size = bttry_size
    
    def fuel_type(self):
        return "Electric charge"
    
mycar = car("Toyota", "corolla")
print(mycar.fuel_type())
tesla = electric_car("tata", "85Kwh")
print(tesla.fuel_type())