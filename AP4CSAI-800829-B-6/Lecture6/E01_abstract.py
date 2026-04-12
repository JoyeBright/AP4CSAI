import abc

class Person(abc.ABC):
   def __init__(self, name, university_id):
       self.name = name
       self.university_id = university_id
   
   @abc.abstractmethod
   def get_role(self):
       pass
