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
    