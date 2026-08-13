#defining global variable
'''x = "sharad khare"

def myfuncion():
    print("My name is " + x)

myfuncion()   
y = "ambika gupta"

def myfunc():
    print("my name is " + y)

myfunc()

#create variable inside a function
def name():
    x = "khare sharad"
    print("My name is " + x)

name()

print("this is " + x)'''
def myfunct():      
    x = "Ambika"  #local variable
    print("my name is " + x)

myfunct()

x = "gupta"  #global variable

print("my surname is " + x) #jb function call hua tb x = ambika value print huyi kyuki priority x
# ki us value ko mili jo function ke andar thi yaha pr overwrite wli cheez nhi huyi or jb function k 
#bahar x ki value gupta krdi or tb print kraya to gupta print huyi