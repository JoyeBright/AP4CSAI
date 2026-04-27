class A:
    def __init__(self):
        self._x = 10 # protected variable

    def print_x(self):
        print(self._x) # accessible internally

a = A()
a.print_x()
print(a._x) # works, but not recommended!

######

class B:
    def __init__(self):
        self._x = 10   # protected variable

class C(B):
    def show(self):
        print(self._x)   # accessible in subclass

c = C()
c.show()
    