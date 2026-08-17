# class laptop:
#     def details(self, brand, ram):
#         self.brand = brand
#         self.ram = ram
#         print(f"Brand is {brand} and RAM is {ram}")
        
# lp1 = laptop()
# lp2 = laptop()

# lp1.details("Dell", "16GB")
# lp2.details("HP", "32GB")

class computer:
    def __init__(self, cpu, ram, ssd):
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
    def config(self):
        print("Config: ", self.cpu, self.ram, self.ssd)
    
com1 = computer("i5", "16GB", "1TB")
com2 = computer("i9", "32GB", "2TB")
    
com1.config()
com2.config()