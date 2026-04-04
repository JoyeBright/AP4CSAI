class A:
    def show(self):
        print("A")   # Base class method


class B(A):
    def show(self):
        super().show()   # Calls A.show() (next in MRO)
        print("B")       # Then prints B


class C(B):
    def show(self):
        super().show()   # Calls B.show() (next in MRO)
        print("C")       # Then prints C


c = C()
c.show()

# print(C.mro())