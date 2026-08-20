class accounts:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name} : {self.balance}"
    def __add__(self, other):
        return f"combined : {self.balance} + {other.balance}"
    def __gt__(self,other):
        return self.balance>other.balance
        
user1 = accounts("Ambika", 1000)
user2 = accounts("Aditya", 2000)
print(user1)
print(user2)
combined = user1+user2
print(combined)
if user1>user2:
    print("Ambika pays the bill")
else:
    print("Aditya pays the bill")