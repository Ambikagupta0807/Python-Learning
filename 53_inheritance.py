class abc:
    def func1(self):
        print("Hello")
class mno(abc):
    def func2(self):
        print("Hii")
class xyz(mno):
    def func3(self):
        print("world")
ob = xyz()
ob.func1()
ob.func2()

# this was multilevel inheritance


class A:
    def f1(self):
        print("F1 works")
class B:
    def f2(self):
        print("F2 works")
class C (A,B):
    def f3 (self):
        print("F3 works")

obj1 = C()
obj1.f2()
obj1.f1()

# this was multiple inheritance


class A:
    def f1(self):
        print("F1 works")
    def show(self):
        print("A shows")
class B:
    def f2(self):
        print("F2 works")
    def show(self):
            print("B shows")
class C (A,B):
    def f3 (self):
        print("F3 works")
    # def show(self):
            # print("C shows")

obj1 = C()
obj1.f2()
obj1.f1()
obj1.show()
# if c also has show then it will always execute show method class C/, if not then :
# obj1.show() if we want to print show() of class A and reverse the order (B,A) if wants to print show of class B
# another way of printing show of class B
B.show(obj1)
