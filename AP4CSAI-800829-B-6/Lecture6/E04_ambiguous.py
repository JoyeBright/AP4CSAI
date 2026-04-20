class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(B, A):
    pass

obj = C()
obj.show()


