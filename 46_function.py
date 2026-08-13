def print_kwargs (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_kwargs(name = "Ambika", age = 21)
print_kwargs(name = "Aditya")
print_kwargs(name = "Adi", age = 22, Year = 2004)
