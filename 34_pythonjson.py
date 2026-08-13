# JSON is a sytax for storing and exchanging the data, it is text which is written with javascript object notation.

# converting from JSON to python
import json 
x = '{"name":"aditya", "age": 21, "city":"baheri"}'
y = json.loads(x)

# the result will be in python dictionary
print(y["age"])

# converting from python to json
import json
x = {"name":"aditya", "age": 21, "city":"baheri"}
y = json.dumps

# the result will be in string
print(y)

# you can convert the following python object to json strings:
# dict, list, tuples, string, int, float, true, false, none

import json
print(json.dumps({"name":"aditya", "age": 21, "city":"baheri"}))
print(json.dumps(["apple", "banana", "cherry"]))
print(json.dumps(("apple", "banana", "cherry")))
print(json.dumps("ambika"))
print(json.dumps(4))
print(json.dumps(44.11))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# when you convert from python to json than python objects are converted into javascript json.
import json
x = {"name":"sharad", "age": 36, "married":True, "divoced": False, "children":("lichi", "chiku"), "pets":None, "cars":[{"model": "bmw 230", "mpg":22.5}, {"model": "ford echo", "mpg":24.1}]}
#x = {"name": "ambika", "age": 21, "married": False, "divorced": False, "children": ("apple", "lichi", "guava"), "pets": None,
#"cars": [{"model": "bmw 230", "mpg": 22.5}, {"model": "ford echo", "mpg": 24.1}]}
# converting into json
y = json.dumps(x)
print(y)


# how to format the result
import json
x = {"name":"sharad", "age": 36, "married":True, "divoced": False, "children":("lichi", "chiku"), "pets":None, "cars":[{"model": "bmw 230", "mpg":22.5}, {"model": "ford echo", "mpg":24.1}]}
# using the 4 indents to make it easier to read
print(json.dumps(x, indent = 4))

# you can also define the seperators meaning comma, colon space.
import json
x = {"name":"sharad", "age": 36, "married":True, "divoced": False, "children":("lichi", "chiku"), "pets":None, "cars":[{"model": "bmw 230", "mpg":22.5}, {"model": "ford echo", "mpg":24.1}]}
print(json.dumps(x, indent=4, sort_keys=True, separators=(" . ", " = ")))

# also you can get the result in specified order
