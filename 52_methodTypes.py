class computer:
    brand = "HP"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def config(self):
        print("The age is : ", self.name, self.age)
        
    @classmethod
    def abc(cls):
        return cls.brand
    
    @staticmethod
    def gb_to_bytes(gb):
        return gb *(1024**3)

com1 = computer("Ambika", 21)
com2 = computer("Aditya", 22)

com1.config()
com2.config()

print(computer.abc())

print(computer.gb_to_bytes(16))