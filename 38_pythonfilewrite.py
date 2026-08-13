# 2 modes for writing in the file
# "a", "w"

# f = open("demofile.txt", "a")
# f.write("we are learning file handling")
# f.close()
# # open and read the file after the appending:
# f = open("demofile.txt", "r")
# print(f.read())

# # 1st open the file and overwrite the content.
# f = open("demofile.txt", "w")
# f.write("this is the new overwritten content of this file")
# f.close()

# # # open and read the file after the appending
# f = open("demofile.txt", "r")
# print(f.read())

# # Creating a new file
# # "x" - create a file
# # "a" - append a file
# # "w" -  will write or create a file


f = open("myfile.txt", "w")
f.write("Hi this is my second file")
f.close()
f = open("myfile.txt", "r")
print(f.read())
f.close()
# # how to delete a file
import os
os.remove("myfile.txt")

# # check if the file exist and give the condition
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("the file does not exists")
# # how to delete the existing folder
import os
os.rmdir("myfolder") # this command can only remove empty folder.