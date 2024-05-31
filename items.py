class Student:
    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tm = None 
        Student.all.append(self)
    
    def __repr__(self):
        return f"Name:{self.name}, TM:{self.tm}"
    
class TM:
    def __init__(self, name):
        self.name = name
        self.students = []  # Define the students attribute
    
    def assign_student(self, student):
        student.tm = self
        self.students.append(student)

    def __repr__(self):
        return f"{self.name}"
    
    def get_students(self):
        return [student for student in Student.all if student.tm == self]
    
barack = Student("Barack Adida", 18)
lapilly = Student("Lapilly Extortionist", 18)
eric = TM("Eric Mong'are")
dennis = TM("Dennis Kiboi")

# Assign students to TM instances
eric.assign_student(barack)
dennis.assign_student(lapilly)

print(Student.all)
print(eric.get_students())
