# What is a Module?
# Consider a module to be as same as a code library like a file containing a set of functions you want to nlcude in a application.

# Create a module.
import mymodule
mymodule.greetings("Aditya")

# variables in Module : A module also contain different variables that can be used in your application.
import mymodule1
a = mymodule1.person1["city"]
print(a)

#naming a module : you can give any name to a module but it should be unique and should not be same as the name of any built in module.
import mymodule as mymodule0
mymodule0.greetings("Ambika")

#platform module : Python has a built in module called platform that can be used to access the underlying platform’s data, such as, hardware, operating system, and interpreter version information.
import platform
x = platform.system()
print(x)

#using the dir() function to list all the function names (or variable names) in a module. The dir() function can be used on all modules, also the ones you create yourself.
import platform
y = dir(platform)
print(y)

z = dir(mymodule0)
print(z)

#import from module : you can choose to import only parts from a module, by using the from keyword.
from mymodule2 import person1
print(person1["age"])
# The module named mymodule2 can now be used without the import keyword. Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule2.person1["age"].