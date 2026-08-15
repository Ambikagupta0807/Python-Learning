x = 2
def func1():
    x = 3
    
print(x)
# It will only print the value of x in global declaration and not in local function declaration bcoz it was never called.

y = 5
def func2():
    print(3)
print(y)
func2()

#it will print both values of y...first of global and then local

z = 6
def funct3():
    print(z)
funct3()

#it will print the value of global declaration of z even though it is printed inside the function because global values are accessible to each function space

x = 99
def func5(y):
    z = x+y
    return z

result = func5(5)
print(result) 
#this also shows that x = 99 is accessable to all as it is global and we are passing value of y while calling function 


m = 10 
def func4():
    global m 
    m = 14
func4()
print (m)
# using global inside a function for making a variable and this practice is recommended to avoid


x = 10
def funca():
    # x = 7
    def funcb():
        print(x)
    funcb()
funca()
#here it will print 7 because it looks for the value step by step so first it took from the function it is in and then global -- it is called climbing

def fi():
    x = 88
    def fj():
        print(x)
    return fj
myres = fi()
myres()

def chaicode(num):
    def actual(x):
        return x**num
    return actual

f = chaicode(2)
g = chaicode(3)

print(f(3))
print(g(3))