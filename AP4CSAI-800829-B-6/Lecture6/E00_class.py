from abc import ABC, abstractmethod

class Person(ABC):
   def __init__(self, name, university_id):
       self.name = name
       self.university_id = university_id

   @abstractmethod
   def get_role(self):
       pass