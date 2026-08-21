# class A:
#     def show(self):
#         print("In A show")
# class B(A):
#     pass        
# obj1 = B()
# obj1.show()
# method B has inherited from method A
# now this method B will have its own show method so it will override the A's show ()
class A:
    def show(self):
        print("In A show")
class B(A):
    def show(self):
        print("In B show")      
obj1 = B()
obj1.show()
