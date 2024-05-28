class User:
    def log_in(self, first, last):
        self.first = first
        self.last = last
    def log_in(self):
        self.logged_in = True
class Student(User):
    def __init__(self, first, last, cohort):
        super().__init__(first, last)
       
        self.cohort = cohort
    def log_in(self):
        super().log_in()
        self.in_class = True

student_1 = Student("barack", "Adida", "SDFT-FT09")
student_1.log_in()

# print(student_1.__dict__)

# user_1 = User()
# user_1.log_in()
# print(user_1.logged_in)
