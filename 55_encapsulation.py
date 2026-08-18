class car:
    def __init__(self, brand, model):
        self.__brand = brand
        self. model = model
    
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"the brand is {self.__brand} and model is {self.model}"
    
mycar = car("Tesla", 2012)
print(mycar.full_name())
# print(mycar.__brand)
print(mycar.get_brand())