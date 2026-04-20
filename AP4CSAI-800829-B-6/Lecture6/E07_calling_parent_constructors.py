from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, university_id):
        print ("Person __init__ is called")
        self.name = name
        self.university_id = university_id
    
    @abstractmethod
    def get_role(self):
        pass

class Student(Person):
    def __init__(self, name, university_id, student_number):
        print ("Student __init__ is called")
        self.student_number = student_number
        Person.__init__(self, name, university_id)
    
    def study(self):
        return f"<{self.name}> is studying"
    
    def get_role(self):
        return "I am a student!"

class Professor(Person):
    def __init__(self, name, university_id, employee_id):
        print ("Professor __init__ is called")
        self.employee_id = employee_id
        Person.__init__(self, name, university_id)
    
    def teach(self):
        return f"<{self.name}> is teaching"
    
    def get_role(self):
        return "I am a professor!"

# Variation C – change the constructor
class TA(Student, Professor):
    def __init__(self, name, university_id, student_number, employee_id):
        super.__init__(self, name, university_id, student_number)
        Professor.__init__(self, name, university_id, employee_id)

    def get_role(self):
        return "I am a teaching assistant!"

ta = TA("Maureen", 123, 1213, 223)
print(ta.employee_id)
print(ta.student_number)


