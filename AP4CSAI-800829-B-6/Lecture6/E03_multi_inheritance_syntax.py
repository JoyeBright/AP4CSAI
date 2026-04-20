class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):
    def showC(self):
        print("Class C (Derived from A and B)")


if __name__ =="__main__":
    obj = C()
    obj.showA()
    obj.showB()
    obj.showC()

