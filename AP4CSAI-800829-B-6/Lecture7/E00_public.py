class A:
    def __init__(self):
        self.x = 10 # public variable

    def print_x(self):
        print(self.x) # accessible internally

a = A()
a.print_x()
print(a.x) # accessible outside the class

######

class B:
    def __init__(self):
        self.x = 10   # public variable

class C(B):
    def show(self):
        print(self.x)   # accessible in subclass

c = C()
c.show()
    