import abc

class Person(abc.ABC):
    def __init__(self, name, university_id):
        print("Person.__init__ called")
        self.name = name
        self.university_id = university_id

    @abc.abstractmethod
    def get_role(self):
        pass


class Student(Person):
    def __init__(self, name, university_id, student_number):
        print("Student.__init__ called")
        self.student_number = student_number
        Person.__init__(self, name, university_id)   # direct call

    def study(self):
        return f"<{self.name}> is studying."

    def get_role(self):
        return "I am a student."


class Professor(Person):
    def __init__(self, name, university_id, employee_id):
        print("Professor.__init__ called")
        self.employee_id = employee_id
        Person.__init__(self, name, university_id)   # direct call

    def teach(self):
        return f"<{self.name}> is teaching."

    def get_role(self):
        return "I am a professor."


class TA(Student, Professor):
    def __init__(self, name, university_id, student_number, employee_id):
        print("TA.__init__ called")
        Student.__init__(self, name, university_id, student_number)
        Professor.__init__(self, name, university_id, employee_id)

    def get_role(self):
        return "I am a teaching assistant."


ta1 = TA("John", 236, 123, 999)