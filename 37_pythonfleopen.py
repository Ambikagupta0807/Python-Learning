# file handling - open()
f = open("demofile.txt")
# or
# isse file ka content read hoga pr print nhi hoga server me
f = open("demofile.txt", "r")

# # there are 4 different modes of opening file
# #"r" it is for reading a file, "a" it is for append, "w" it is for writing in a file, "x"

# # to open the file using built in open() and read()
# isse file ka jo content h wo read hoke print ho jayega
f = open("demofile.txt", "r")
print(f.read())
# # # open a file in different location
f = open(r"C:\Users\ambikagupta__\Documents\PY\PY\demofile.txt", "r")
print(f.read())

# # # # read only parts of the file
f = open(r"C:\Users\ambikagupta__\Documents\PY\PY\demofile.txt", "r")
print(f.read(6))

# # # how to read lines one by one using readline()
f = open(r"C:\Users\ambikagupta__\Documents\PY\PY\demofile.txt", "r")
print(f.readline())
print(f.readline())


# # # looping through the line by line using for loop:
f = open(r"C:\Users\ambikagupta__\Documents\PY\PY\demofile.txt", "r")
for i in f:
    print(i)


# # How to close the open file
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()
