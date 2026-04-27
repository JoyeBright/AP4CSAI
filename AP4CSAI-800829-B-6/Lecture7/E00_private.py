class A:
    def __init__(self):
        self.__x = 10 # private variable

    def print_x(self):
        print(self.__x) # accessible internally

a = A()
a.print_x()
print(a.__x) # does not work. Not accessible outside

######

class B:
    def __init__(self):
        self.__x = 10   # private variable

class C(B):
    def show(self):
        print(self.__x)   # does not work. Not accessible subclass

c = C()
c.show()
    