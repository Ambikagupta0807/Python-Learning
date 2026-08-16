#inner function 
def outer():
    print("outer")
    def inner():
        print("inner")
    
some = outer()
print(some)

# Decorators --  traditional way(without @)

def greater_first(func):
    def wrap(a,b):
        a , b = b ,a 
        return func(a,b)
    return wrap

def sub(a,b):
    return a - b

def div(a,b):
    return a/b

sub = greater_first(sub)
res = sub(2,4)
print(res)

div = greater_first(div)
res1 = div(2,4)
print(res1)

# decorators -- modern way(with @)
def log_info(func):
    def wrap(*args, **kwargs):
        print("values are ", args)
        result = func(*args)
        print("Result", result)
        return result
    return wrap

def greater_first(func):
    def wrap(a,b):
        a , b = b ,a 
        return func(a,b)
    
    return wrap

@log_info
@greater_first
def sub(a,b):
    return a - b

@log_info
@greater_first
def div(a,b):
    return a/b

@log_info
def add(*args):
    return sum(args)



# sub = greater_first(sub)
res = sub(2,4)
print(res)

# div = greater_first(div)
res1 = div(2,4)
print(res1)

res2 = add(2,4,7)
print(res2)
